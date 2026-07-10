import { browser } from 'wxt/browser';
import {
  extractProfileFromDom,
  extractProfileFromPayload,
  extractVideosFromDom,
  extractVideosFromPayload,
} from '../lib/tiktok-parser';
import type { ProfileRecord, RuntimeMessage, ScanOptions, ScanState, VideoRecord } from '../lib/types';

let scanning = false;
let stopRequested = false;
let currentUsername = '';

function getProfileContext(): { username: string; profileUrl: string } | undefined {
  const match = location.pathname.match(/^\/@([^/]+)/);
  const username = match?.[1]?.replace(/^@/, '');
  if (!username) return undefined;
  return { username, profileUrl: `https://www.tiktok.com/@${username}` };
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
  (document.head || document.documentElement).append(script);
}

async function sendBatch(username: string, profileUrl: string, videos: VideoRecord[]): Promise<void> {
  if (!videos.length) return;
  await browser.runtime.sendMessage({ type: 'VIDEO_BATCH', username, profileUrl, videos } satisfies RuntimeMessage);
}

async function sendProfile(profile: ProfileRecord | undefined): Promise<void> {
  if (!profile) return;
  await browser.runtime.sendMessage({ type: 'PROFILE_DATA', profile } satisfies RuntimeMessage);
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
    document.querySelector('[id*="captcha" i], iframe[src*="captcha" i], [class*="captcha" i]') ||
    text.includes('verify to continue') ||
    text.includes('подтвердите, что вы человек')
  );
}

async function collectEmbeddedJson(username: string, profileUrl: string): Promise<void> {
  const candidates = [
    document.querySelector<HTMLScriptElement>('#__UNIVERSAL_DATA_FOR_REHYDRATION__'),
    document.querySelector<HTMLScriptElement>('#SIGI_STATE'),
  ].filter(Boolean) as HTMLScriptElement[];

  for (const script of candidates) {
    try {
      const payload = JSON.parse(script.textContent ?? '{}');
      await Promise.all([
        sendBatch(username, profileUrl, extractVideosFromPayload(payload, username, 'embedded-json')),
        sendProfile(extractProfileFromPayload(payload, username, 'embedded-json')),
      ]);
    } catch {
      // A changed or non-JSON bootstrap payload is not fatal.
    }
  }
}

async function collectProfileDom(username: string): Promise<void> {
  await sendProfile(extractProfileFromDom(username));
}

async function startScan(options: ScanOptions): Promise<void> {
  if (scanning) return;
  const context = getProfileContext();
  if (!context) {
    await sendState({ status: 'error', videosFound: 0, message: 'Откройте публичный профиль TikTok.' });
    return;
  }

  scanning = true;
  stopRequested = false;
  currentUsername = context.username;
  const startedAt = Date.now();
  let idleRounds = 0;
  let lastCount = 0;
  let oldestPublishedAt: number | undefined;

  injectPageHook();
  await sendState({
    status: 'scanning',
    username: context.username,
    profileUrl: context.profileUrl,
    videosFound: 0,
    startedAt,
    message: 'Сканирование профиля…',
  });

  await Promise.all([
    collectEmbeddedJson(context.username, context.profileUrl),
    collectProfileDom(context.username),
  ]);

  while (!stopRequested) {
    if (detectChallenge()) {
      await sendState({
        status: 'blocked',
        username: context.username,
        profileUrl: context.profileUrl,
        videosFound: lastCount,
        startedAt,
        oldestPublishedAt,
        message: 'TikTok запросил проверку. Пройдите её вручную и запустите сканирование снова.',
      });
      break;
    }

    const domVideos = extractVideosFromDom(context.username);
    await Promise.all([
      sendBatch(context.username, context.profileUrl, domVideos),
      collectProfileDom(context.username),
    ]);
    const dates = domVideos.map((video) => video.publishedAt).filter((value): value is number => Boolean(value));
    if (dates.length) oldestPublishedAt = Math.min(oldestPublishedAt ?? Infinity, ...dates);

    const currentCount = new Set(domVideos.map((video) => video.id)).size;
    idleRounds = currentCount <= lastCount ? idleRounds + 1 : 0;
    lastCount = Math.max(lastCount, currentCount);

    await sendState({
      status: 'scanning',
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
        username: context.username,
        profileUrl: context.profileUrl,
        videosFound: lastCount,
        startedAt,
        oldestPublishedAt,
        message: idleRounds >= options.maxIdleRounds ? 'Новые ролики перестали загружаться.' : 'Достигнут заданный лимит.',
      });
      break;
    }

    window.scrollTo({ top: document.documentElement.scrollHeight, behavior: 'smooth' });
    await new Promise((resolve) => setTimeout(resolve, options.scrollDelayMs));
  }

  if (stopRequested) {
    await sendState({
      status: 'stopped',
      username: context.username,
      profileUrl: context.profileUrl,
      videosFound: lastCount,
      startedAt,
      oldestPublishedAt,
      message: 'Сканирование остановлено пользователем.',
    });
  }

  scanning = false;
  stopRequested = false;
}

export default defineContentScript({
  matches: ['https://www.tiktok.com/@*', 'https://tiktok.com/@*'],
  runAt: 'document_start',
  main(ctx) {
    const runtimeMarker = '__TIKTOK_RESEARCH_SORTER_CONTENT_READY__';
    const globalObject = globalThis as typeof globalThis & Record<string, unknown>;
    if (globalObject[runtimeMarker]) return;
    globalObject[runtimeMarker] = true;

    injectPageHook();

    ctx.addEventListener(window, 'message', (event: MessageEvent) => {
      if (!scanning || event.source !== window) return;
      const data = event.data as { source?: string; type?: string; payload?: unknown };
      if (data.source !== 'tiktok-research-sorter-page-hook' || data.type !== 'TIKTOK_API_PAYLOAD') return;
      const context = getProfileContext();
      if (!context || context.username !== currentUsername) return;
      const videos = extractVideosFromPayload(data.payload, context.username, 'api');
      const profile = extractProfileFromPayload(data.payload, context.username, 'api');
      void Promise.all([
        sendBatch(context.username, context.profileUrl, videos),
        sendProfile(profile),
      ]);
    });

    browser.runtime.onMessage.addListener((message: RuntimeMessage) => {
      if (message.type === 'PING') return Promise.resolve({ ok: true, context: getProfileContext() });
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
