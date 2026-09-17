export const DOWNLOAD_MANAGER_ORIGIN = 'http://127.0.0.1:8000';
export const DOWNLOAD_MANAGER_JOBS_ENDPOINT = `${DOWNLOAD_MANAGER_ORIGIN}/api/jobs`;

export interface DownloadQueueResult {
  jobId?: string;
  title?: string;
  status?: string;
}

type FetchLike = (input: string, init?: RequestInit) => Promise<Response>;

function assertTikTokVideoUrl(value: string): string {
  let parsed: URL;
  try {
    parsed = new URL(value);
  } catch {
    throw new Error('Некорректная ссылка на TikTok-ролик.');
  }

  const hostname = parsed.hostname.toLowerCase();
  const isTikTokHost = hostname === 'tiktok.com' || hostname.endsWith('.tiktok.com');
  if (parsed.protocol !== 'https:' || !isTikTokHost || !parsed.pathname.includes('/video/')) {
    throw new Error('Скачивание доступно только для прямых ссылок на публичные TikTok-ролики.');
  }

  return parsed.toString();
}

function responseDetail(payload: unknown): string | undefined {
  if (!payload || typeof payload !== 'object') return undefined;
  const candidate = payload as { detail?: unknown; error?: unknown; message?: unknown };
  for (const value of [candidate.detail, candidate.error, candidate.message]) {
    if (typeof value === 'string' && value.trim()) return value.trim();
  }
  return undefined;
}

export async function queueTikTokDownload(
  videoUrl: string,
  fetchImpl: FetchLike = fetch,
): Promise<DownloadQueueResult> {
  const url = assertTikTokVideoUrl(videoUrl);

  let response: Response;
  try {
    response = await fetchImpl(DOWNLOAD_MANAGER_JOBS_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        url,
        mode: 'video',
        quality: 'bestvideo*+bestaudio/best',
      }),
    });
  } catch (cause) {
    const details = cause instanceof Error ? cause.message : String(cause);
    throw new Error(`Локальный Download Manager недоступен. Запустите Yt-Dlp-Download-Manager на ${DOWNLOAD_MANAGER_ORIGIN}. ${details}`);
  }

  let payload: unknown;
  try {
    payload = await response.json();
  } catch {
    payload = undefined;
  }

  if (!response.ok) {
    throw new Error(responseDetail(payload) || `Download Manager вернул ошибку HTTP ${response.status}.`);
  }

  const job = payload && typeof payload === 'object'
    ? (payload as { job?: { id?: unknown; title?: unknown; status?: unknown } }).job
    : undefined;

  return {
    jobId: typeof job?.id === 'string' ? job.id : undefined,
    title: typeof job?.title === 'string' ? job.title : undefined,
    status: typeof job?.status === 'string' ? job.status : undefined,
  };
}
