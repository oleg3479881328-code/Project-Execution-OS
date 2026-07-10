export default defineUnlistedScript(() => {
  const marker = '__TIKTOK_RESEARCH_SORTER_HOOKED__';
  const globalObject = window as typeof window & Record<string, unknown>;
  if (globalObject[marker]) return;
  globalObject[marker] = true;

  const shouldInspect = (url: string) =>
    url.includes('/api/post/item_list/') ||
    url.includes('/api/user/detail/') ||
    url.includes('/api/item/detail/');

  const emit = (url: string, payload: unknown) => {
    window.postMessage({
      source: 'tiktok-research-sorter-page-hook',
      type: 'TIKTOK_API_PAYLOAD',
      url,
      payload,
    }, '*');
  };

  const originalFetch = window.fetch.bind(window);
  window.fetch = async (...args) => {
    const response = await originalFetch(...args);
    try {
      const request = args[0];
      const url = typeof request === 'string' ? request : request instanceof Request ? request.url : '';
      if (shouldInspect(url)) {
        void response.clone().json().then((payload) => emit(url, payload)).catch(() => undefined);
      }
    } catch {
      // TikTok must keep working even if inspection fails.
    }
    return response;
  };

  const OriginalXhr = window.XMLHttpRequest;
  const originalOpen = OriginalXhr.prototype.open;
  const originalSend = OriginalXhr.prototype.send;

  OriginalXhr.prototype.open = function(method: string, url: string | URL, ...rest: unknown[]) {
    (this as XMLHttpRequest & { __trsUrl?: string }).__trsUrl = String(url);
    return (originalOpen as (...args: unknown[]) => void).call(this, method, url, ...rest);
  };

  OriginalXhr.prototype.send = function(...args: Parameters<XMLHttpRequest['send']>) {
    this.addEventListener('load', () => {
      try {
        const url = (this as XMLHttpRequest & { __trsUrl?: string }).__trsUrl ?? '';
        if (!shouldInspect(url) || typeof this.responseText !== 'string') return;
        emit(url, JSON.parse(this.responseText));
      } catch {
        // Ignore non-JSON or protected responses.
      }
    });
    return originalSend.apply(this, args);
  };
});
