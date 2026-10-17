import { describe, expect, it, vi } from 'vitest';
import {
  DOWNLOAD_MANAGER_JOBS_ENDPOINT,
  queueTikTokDownload,
} from '../lib/download-manager';

describe('queueTikTokDownload', () => {
  it('queues a public TikTok video through the existing local Download Manager API', async () => {
    const fetchMock = vi.fn(async () => new Response(JSON.stringify({
      ok: true,
      job: {
        id: 'job-123',
        title: 'Test TikTok video',
        status: 'queued',
      },
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    }));

    const result = await queueTikTokDownload(
      'https://www.tiktok.com/@creator/video/7461234567890123456',
      fetchMock,
    );

    expect(result).toEqual({
      jobId: 'job-123',
      title: 'Test TikTok video',
      status: 'queued',
    });
    expect(fetchMock).toHaveBeenCalledOnce();
    expect(fetchMock).toHaveBeenCalledWith(DOWNLOAD_MANAGER_JOBS_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        url: 'https://www.tiktok.com/@creator/video/7461234567890123456',
        mode: 'video',
        quality: 'bestvideo*+bestaudio/best',
      }),
    });
  });

  it('rejects non-TikTok and non-video URLs before calling the local service', async () => {
    const fetchMock = vi.fn();

    await expect(queueTikTokDownload('https://example.com/video/123', fetchMock))
      .rejects.toThrow('Скачивание доступно только для прямых ссылок на публичные TikTok-ролики.');
    await expect(queueTikTokDownload('https://www.tiktok.com/@creator', fetchMock))
      .rejects.toThrow('Скачивание доступно только для прямых ссылок на публичные TikTok-ролики.');

    expect(fetchMock).not.toHaveBeenCalled();
  });

  it('surfaces the Download Manager API error detail', async () => {
    const fetchMock = vi.fn(async () => new Response(JSON.stringify({
      detail: 'Video is unavailable',
    }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' },
    }));

    await expect(queueTikTokDownload(
      'https://www.tiktok.com/@creator/video/7461234567890123456',
      fetchMock,
    )).rejects.toThrow('Video is unavailable');
  });

  it('explains how to start the local manager when the service is unavailable', async () => {
    const fetchMock = vi.fn(async () => {
      throw new TypeError('Failed to fetch');
    });

    await expect(queueTikTokDownload(
      'https://www.tiktok.com/@creator/video/7461234567890123456',
      fetchMock,
    )).rejects.toThrow('Запустите Yt-Dlp-Download-Manager на http://127.0.0.1:8000');
  });
});
