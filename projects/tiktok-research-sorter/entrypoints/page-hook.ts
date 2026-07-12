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

  OriginalXhr.prototype.open = function(method: string, url: string | URL, ...rest: unknown[]) {
    const targetUrl = String(url);
    if (shouldInspect(targetUrl)) {
      this.addEventListener('load', () => {
        try {
          if (typeof this.responseText !== 'string') return;
          emit(targetUrl, JSON.parse(this.responseText));
        } catch {
          // Ignore non-JSON or protected responses.
        }
      }, { once: true });
    }
    return (originalOpen as (...args: unknown[]) => void).call(this, method, url, ...rest);
  };
});
