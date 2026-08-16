export async function captureRaw(url) {
  const response = await fetch(url, { redirect: 'follow', headers: { 'user-agent': 'website-intelligence-mvp/0.1 (research; contact unavailable)' } });
  return { status: response.status, finalUrl: response.url, headers: Object.fromEntries(response.headers), html: await response.text() };
}
