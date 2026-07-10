import { browser } from 'wxt/browser';
import { extractVideosFromDom, extractVideosFromPayload } from '../lib/tiktok-parser';
import type { RuntimeMessage, ScanOptions, ScanState, VideoRecord } from '../lib/types';

let scanning = false;
let stopRequested = false;
let currentUsername = '';

function getProfileContext(): { username: string; profileUrl: string } | undefined {
  const match = location.pathname.match(/^\/@([^/]+)/);
  const username = match?.[1]?.replace(/^@/, '');
  if (!username) return undefined;
  return { username, profileUrl: `${location.origin}/@${username}` };
}

function injectPageHook(): void {
  if (document.documentElement.dataset.trsHookInjected === 'true') return;
  document.documentElement.dataset.trsHookInjected = 'true';
  const script = document.createElement('script');
  script.src = browser.runtime.getURL('/page-hook.js');
  script.onload = () => script.remove();
  (document.head || document.documentElement).append(script);
}

async function sendBatch(username: string, profileUrl: string, videos: VideoRecord[]): Promise<void> {
  if (!videos.length) return;
  await browser.runtime.sendMessage({ type: 'VIDEO_BATCH', username, profileUrl, videos } satisfies RuntimeMessage);
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
      await sendBatch(username, profileUrl, extractVideosFromPayload(payload, username, 'embedded-json'));
    } catch {
      // A changed or non-JSON bootstrap payload is not fatal.
    }
  }
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

  await collectEmbeddedJson(context.username, context.profileUrl);

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
    await sendBatch(context.username, context.profileUrl, domVideos);
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
  matches: ['https://www.tiktok.com/@*'],
  runAt: 'document_start',
  main(ctx) {
    injectPageHook();

    ctx.addEventListener(window, 'message', (event: MessageEvent) => {
      if (!scanning || event.source !== window) return;
      const data = event.data as { source?: string; type?: string; payload?: unknown };
      if (data.source !== 'tiktok-research-sorter-page-hook' || data.type !== 'TIKTOK_API_PAYLOAD') return;
      const context = getProfileContext();
      if (!context || context.username !== currentUsername) return;
      const videos = extractVideosFromPayload(data.payload, context.username, 'api');
      void sendBatch(context.username, context.profileUrl, videos);
    });

    browser.runtime.onMessage.addListener((message: RuntimeMessage) => {
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
