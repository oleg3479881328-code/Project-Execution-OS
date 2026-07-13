import { browser } from 'wxt/browser';
import {
  extractProfileFromDom,
  extractProfileFromPayload,
  extractVideosFromDiscoveryDom,
  extractVideosFromDom,
  extractVideosFromPayload,
  mergeVideoRecords,
} from '../lib/tiktok-parser';
import type {
  ProfilePageContext,
  ProfileRecord,
  RuntimeMessage,
  ScanOptions,
  ScanState,
  TagPageContext,
  TikTokPageContext,
  VideoRecord,
} from '../lib/types';

let scanning = false;
let stopRequested = false;
let currentContext: TikTokPageContext | undefined;
let currentTagVideos: Map<string, VideoRecord> | undefined;

function getPageContext(): TikTokPageContext | undefined {
  const profileMatch = location.pathname.match(/^\/@([^/]+)/i);
  const username = profileMatch?.[1]?.replace(/^@/, '');
  if (username) {
    return { kind: 'profile', username, profileUrl: `https://www.tiktok.com/@${username}` };
  }

  const tagMatch = location.pathname.match(/^\/tag\/([^/?#]+)/i);
  const tag = tagMatch?.[1] ? decodeURIComponent(tagMatch[1]).replace(/^#/, '') : '';
  if (tag) {
    return { kind: 'tag', tag, tagUrl: `https://www.tiktok.com/tag/${encodeURIComponent(tag)}` };
  }

  return undefined;
}

function injectPageHook(): void {
  const root = document.documentElement;
  if (!root) {
    document.addEventListener('readystatechange', injectPageHook, { once: true });
    return;
  }
  if (root.dataset.trsHookInjected === 'true') return;
  root.dataset.trsHookInjected = 'true';
  const script = document.createElement('script');
  script.src = browser.runtime.getURL('/page-hook.js');
  script.onload = () => script.remove();
  script.onerror = () => script.remove();
  (document.head || document.documentElement).append(script);
}

async function sendProfileBatch(context: ProfilePageContext, videos: VideoRecord[]): Promise<void> {
  if (!videos.length) return;
  await browser.runtime.sendMessage({
    type: 'VIDEO_BATCH',
    username: context.username,
    profileUrl: context.profileUrl,
    videos,
  } satisfies RuntimeMessage);
}

async function sendProfile(profile: ProfileRecord | undefined): Promise<void> {
  if (!profile) return;
  await browser.runtime.sendMessage({ type: 'PROFILE_DATA', profile } satisfies RuntimeMessage);
}

function mergeCurrentTagVideos(videos: VideoRecord[]): void {
  if (!currentTagVideos) return;
  for (const video of videos) {
    const key = `${video.author.toLowerCase()}:${video.id}`;
    const existing = currentTagVideos.get(key);
    currentTagVideos.set(key, existing ? mergeVideoRecords(existing, video) : video);
  }
}

async function sendTagBatch(context: TagPageContext, videos: VideoRecord[]): Promise<void> {
  if (!videos.length) return;
  mergeCurrentTagVideos(videos);
  await browser.runtime.sendMessage({
    type: 'TAG_VIDEO_BATCH',
    tag: context.tag,
    tagUrl: context.tagUrl,
    videos,
  } satisfies RuntimeMessage);
}

async function sendState(state: Omit<ScanState, 'updatedAt'>): Promise<void> {
  await browser.runtime.sendMessage({
    type: 'SCAN_STATE',
    state: { ...state, updatedAt: Date.now() },
  } satisfies RuntimeMessage);
}

function detectChallenge(): boolean {
  const text = document.body?.innerText.toLowerCase() ?? '';
  return Boolean(
    document.querySelector('[id*="captcha" i], iframe[src*="captcha" i], [class*="captcha" i]')
    || text.includes('verify to continue')
    || text.includes('подтвердите, что вы человек')
  );
}

function embeddedPayloads(): unknown[] {
  const candidates = [
    document.querySelector<HTMLScriptElement>('#__UNIVERSAL_DATA_FOR_REHYDRATION__'),
    document.querySelector<HTMLScriptElement>('#SIGI_STATE'),
  ].filter(Boolean) as HTMLScriptElement[];

  return candidates.flatMap((script) => {
    try {
      return [JSON.parse(script.textContent ?? '{}')];
    } catch {
      return [];
    }
  });
}

async function collectProfileEmbedded(context: ProfilePageContext): Promise<void> {
  for (const payload of embeddedPayloads()) {
    await Promise.all([
      sendProfileBatch(context, extractVideosFromPayload(payload, context.username, 'embedded-json')),
      sendProfile(extractProfileFromPayload(payload, context.username, 'embedded-json')),
    ]);
  }
}

async function collectTagEmbedded(context: TagPageContext): Promise<void> {
  for (const payload of embeddedPayloads()) {
    await sendTagBatch(context, extractVideosFromPayload(payload, '', 'embedded-json'));
  }
}

async function collectProfileDom(context: ProfilePageContext): Promise<void> {
  await sendProfile(extractProfileFromDom(context.username));
}

async function startProfileScan(context: ProfilePageContext, options: ScanOptions): Promise<void> {
  const startedAt = Date.now();
  let idleRounds = 0;
  let lastCount = 0;
  let oldestPublishedAt: number | undefined;

  await sendState({
    status: 'scanning',
    mode: 'profile',
    username: context.username,
    profileUrl: context.profileUrl,
    videosFound: 0,
    startedAt,
    message: 'Сканирование профиля…',
  });

  await Promise.all([collectProfileEmbedded(context), collectProfileDom(context)]);

  while (!stopRequested) {
    if (detectChallenge()) {
      await sendState({
        status: 'blocked',
        mode: 'profile',
        username: context.username,
        profileUrl: context.profileUrl,
        videosFound: lastCount,
        startedAt,
        oldestPublishedAt,
        message: 'TikTok запросил проверку. Пройдите её вручную и запустите сканирование снова.',
      });
      return;
    }

    const domVideos = extractVideosFromDom(context.username);
    await Promise.all([sendProfileBatch(context, domVideos), collectProfileDom(context)]);
    const dates = domVideos.map((video) => video.publishedAt).filter((value): value is number => Boolean(value));
    if (dates.length) oldestPublishedAt = Math.min(oldestPublishedAt ?? Infinity, ...dates);

    const currentCount = new Set(domVideos.map((video) => video.id)).size;
    idleRounds = currentCount <= lastCount ? idleRounds + 1 : 0;
    lastCount = Math.max(lastCount, currentCount);

    await sendState({
      status: 'scanning',
      mode: 'profile',
      username: context.username,
      profileUrl: context.profileUrl,
      videosFound: lastCount,
      startedAt,
      oldestPublishedAt,
      message: `Найдено на странице: ${lastCount}. Загружаю дальше…`,
    });

    if (lastCount >= options.maxVideos || idleRounds >= options.maxIdleRounds) {
      await sendState({
        status: 'complete',
        mode: 'profile',
        username: context.username,
        profileUrl: context.profileUrl,
        videosFound: lastCount,
        startedAt,
        oldestPublishedAt,
        message: idleRounds >= options.maxIdleRounds ? 'Новые ролики перестали загружаться.' : 'Достигнут заданный лимит.',
      });
      return;
    }

    window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' });
    await new Promise((resolve) => setTimeout(resolve, options.scrollDelayMs));
  }

  await sendState({
    status: 'stopped',
    mode: 'profile',
    username: context.username,
    profileUrl: context.profileUrl,
    videosFound: lastCount,
    startedAt,
    oldestPublishedAt,
    message: 'Сканирование остановлено пользователем.',
  });
}

async function startTagScan(context: TagPageContext, options: ScanOptions): Promise<void> {
  const startedAt = Date.now();
  let idleRounds = 0;
  let lastCount = 0;
  currentTagVideos = new Map();

  await browser.runtime.sendMessage({
    type: 'TAG_SCAN_BEGIN',
    tag: context.tag,
    tagUrl: context.tagUrl,
    options,
  } satisfies RuntimeMessage);

  await sendState({
    status: 'scanning',
    mode: 'tag',
    tag: context.tag,
    tagUrl: context.tagUrl,
    videosFound: 0,
    accountsFound: 0,
    startedAt,
    message: `Сканирование #${context.tag}…`,
  });

  await collectTagEmbedded(context);

  while (!stopRequested) {
    if (detectChallenge()) {
      const accountsFound = new Set([...(currentTagVideos?.values() ?? [])].map((video) => video.author.toLowerCase())).size;
      await sendState({
        status: 'blocked',
        mode: 'tag',
        tag: context.tag,
        tagUrl: context.tagUrl,
        videosFound: currentTagVideos?.size ?? lastCount,
        accountsFound,
        startedAt,
        message: 'TikTok запросил проверку. Пройдите её вручную и запустите сканирование снова.',
      });
      return;
    }

    await sendTagBatch(context, extractVideosFromDiscoveryDom());
    const currentCount = currentTagVideos?.size ?? 0;
    const accountsFound = new Set([...(currentTagVideos?.values() ?? [])].map((video) => video.author.toLowerCase())).size;
    idleRounds = currentCount <= lastCount ? idleRounds + 1 : 0;
    lastCount = Math.max(lastCount, currentCount);

    await sendState({
      status: 'scanning',
      mode: 'tag',
      tag: context.tag,
      tagUrl: context.tagUrl,
      videosFound: currentCount,
      accountsFound,
      startedAt,
      message: `Найдено ${currentCount} роликов из ${accountsFound} аккаунтов. Загружаю дальше…`,
    });

    if (currentCount >= options.maxVideos || idleRounds >= options.maxIdleRounds) {
      await sendState({
        status: 'complete',
        mode: 'tag',
        tag: context.tag,
        tagUrl: context.tagUrl,
        videosFound: currentCount,
        accountsFound,
        startedAt,
        message: idleRounds >= options.maxIdleRounds
          ? `Сканирование #${context.tag} завершено: новые ролики перестали загружаться.`
          : `Сканирование #${context.tag} завершено по лимиту.`,
      });
      return;
    }

    window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' });
    await new Promise((resolve) => setTimeout(resolve, options.scrollDelayMs));
  }

  const accountsFound = new Set([...(currentTagVideos?.values() ?? [])].map((video) => video.author.toLowerCase())).size;
  await sendState({
    status: 'stopped',
    mode: 'tag',
    tag: context.tag,
    tagUrl: context.tagUrl,
    videosFound: currentTagVideos?.size ?? lastCount,
    accountsFound,
    startedAt,
    message: 'Сканирование хэштега остановлено пользователем.',
  });
}

async function startScan(options: ScanOptions): Promise<void> {
  if (scanning) return;
  const context = getPageContext();
  if (!context) {
    await sendState({
      status: 'error',
      videosFound: 0,
      message: 'Откройте публичный профиль TikTok или страницу хэштега TikTok.',
    });
    return;
  }

  scanning = true;
  stopRequested = false;
  currentContext = context;

  try {
    injectPageHook();
    if (context.kind === 'profile') await startProfileScan(context, options);
    else await startTagScan(context, options);
  } catch (cause) {
    const details = cause instanceof Error ? cause.message : String(cause);
    const tagValues = [...(currentTagVideos?.values() ?? [])];
    await sendState({
      status: 'error',
      mode: context.kind,
      username: context.kind === 'profile' ? context.username : undefined,
      profileUrl: context.kind === 'profile' ? context.profileUrl : undefined,
      tag: context.kind === 'tag' ? context.tag : undefined,
      tagUrl: context.kind === 'tag' ? context.tagUrl : undefined,
      videosFound: context.kind === 'tag' ? tagValues.length : 0,
      accountsFound: context.kind === 'tag' ? new Set(tagValues.map((video) => video.author.toLowerCase())).size : undefined,
      message: `Сканирование прервано: ${details}`,
    }).catch(() => undefined);
  } finally {
    scanning = false;
    stopRequested = false;
    currentContext = undefined;
    currentTagVideos = undefined;
  }
}

export default defineContentScript({
  matches: [
    'https://www.tiktok.com/@*',
    'https://tiktok.com/@*',
    'https://www.tiktok.com/tag/*',
    'https://tiktok.com/tag/*',
  ],
  runAt: 'document_start',
  main(ctx) {
    const runtimeMarker = '__TIKTOK_RESEARCH_SORTER_CONTENT_READY__';
    const globalObject = globalThis as typeof globalThis & Record<string, unknown>;
    if (globalObject[runtimeMarker]) return;
    globalObject[runtimeMarker] = true;

    injectPageHook();

    ctx.addEventListener(window, 'message', (event: MessageEvent) => {
      if (!scanning || event.source !== window || !currentContext) return;
      const data = event.data as { source?: string; type?: string; payload?: unknown };
      if (data.source !== 'tiktok-research-sorter-page-hook' || data.type !== 'TIKTOK_API_PAYLOAD') return;

      if (currentContext.kind === 'profile') {
        const pageContext = getPageContext();
        if (pageContext?.kind !== 'profile' || pageContext.username !== currentContext.username) return;
        const videos = extractVideosFromPayload(data.payload, currentContext.username, 'api');
        const profile = extractProfileFromPayload(data.payload, currentContext.username, 'api');
        void Promise.all([
          sendProfileBatch(currentContext, videos),
          sendProfile(profile),
        ]).catch(() => undefined);
        return;
      }

      const pageContext = getPageContext();
      if (pageContext?.kind !== 'tag' || pageContext.tag.toLowerCase() !== currentContext.tag.toLowerCase()) return;
      void sendTagBatch(currentContext, extractVideosFromPayload(data.payload, '', 'api')).catch(() => undefined);
    });

    browser.runtime.onMessage.addListener((message: RuntimeMessage) => {
      if (message.type === 'PING') return Promise.resolve({ ok: true, context: getPageContext() });
      if (message.type === 'START_SCAN') {
        void startScan(message.options);
        return Promise.resolve({ ok: true });
      }
      if (message.type === 'STOP_SCAN') {
        stopRequested = true;
        return Promise.resolve({ ok: true });
      }
      return undefined;
    });
  },
});
