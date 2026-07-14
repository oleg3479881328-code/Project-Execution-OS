import { useEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { browser } from 'wxt/browser';
import type { DownloadQueueResponse, RuntimeMessage } from '../../lib/types';

type DownloadState = 'idle' | 'sending' | 'queued' | 'error';

interface DownloadTarget {
  key: string;
  slot: HTMLElement;
  videoUrl: string;
}

function targetSignature(targets: DownloadTarget[]): string {
  return targets.map((target) => `${target.key}:${target.videoUrl}`).join('|');
}

function collectTargets(): DownloadTarget[] {
  const targets: DownloadTarget[] = [];

  document.querySelectorAll<HTMLElement>('.video-card').forEach((card, index) => {
    const cover = card.querySelector<HTMLAnchorElement>('a.cover[href]');
    const copy = card.querySelector<HTMLElement>('.video-copy');
    const videoUrl = cover?.href;

    if (!copy || !videoUrl || !videoUrl.includes('tiktok.com/') || !videoUrl.includes('/video/')) return;

    let slot = copy.querySelector<HTMLElement>(':scope > .download-control-slot');
    if (!slot) {
      slot = document.createElement('div');
      slot.className = 'download-control-slot';
      copy.append(slot);
    }

    targets.push({
      key: card.dataset.downloadKey || `${videoUrl}:${index}`,
      slot,
      videoUrl,
    });
  });

  return targets;
}

function DownloadButton({ videoUrl }: { videoUrl: string }) {
  const [state, setState] = useState<DownloadState>('idle');
  const [message, setMessage] = useState('');

  const startDownload = async () => {
    if (state === 'sending') return;

    setState('sending');
    setMessage('');

    try {
      const response = await browser.runtime.sendMessage({
        type: 'DOWNLOAD_VIDEO',
        videoUrl,
      } satisfies RuntimeMessage) as DownloadQueueResponse;

      if (!response?.ok) throw new Error(response?.error || 'Не удалось поставить ролик в очередь.');

      setState('queued');
      setMessage(response.title ? `В очереди: ${response.title}` : 'Ролик добавлен в очередь Download Manager.');
    } catch (cause) {
      setState('error');
      setMessage(cause instanceof Error ? cause.message : String(cause));
    }
  };

  const label = state === 'sending'
    ? 'Отправляем…'
    : state === 'queued'
      ? '✓ В очереди'
      : state === 'error'
        ? 'Повторить'
        : '↓ Скачать';

  return (
    <div className={`download-control download-control-${state}`}>
      <button
        type="button"
        className="download-button"
        onClick={() => void startDownload()}
        disabled={state === 'sending'}
        title="Скачать через локальный Yt-Dlp-Download-Manager"
      >
        {label}
      </button>
      {message && <span className="download-message" title={message}>{message}</span>}
    </div>
  );
}

export default function VideoDownloadControls() {
  const [targets, setTargets] = useState<DownloadTarget[]>([]);
  const scheduled = useRef<number | undefined>(undefined);

  useEffect(() => {
    const refresh = () => {
      if (scheduled.current !== undefined) window.cancelAnimationFrame(scheduled.current);
      scheduled.current = window.requestAnimationFrame(() => {
        const next = collectTargets();
        setTargets((current) => targetSignature(current) === targetSignature(next) ? current : next);
      });
    };

    refresh();

    const observer = new MutationObserver(refresh);
    observer.observe(document.getElementById('root') || document.body, {
      childList: true,
      subtree: true,
    });

    return () => {
      observer.disconnect();
      if (scheduled.current !== undefined) window.cancelAnimationFrame(scheduled.current);
    };
  }, []);

  return (
    <>
      {targets.map((target) => createPortal(
        <DownloadButton videoUrl={target.videoUrl} />,
        target.slot,
        target.key,
      ))}
    </>
  );
}
