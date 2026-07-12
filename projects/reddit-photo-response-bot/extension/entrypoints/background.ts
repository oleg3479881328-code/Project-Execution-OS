export default defineBackground(() => {
  if (!chrome.sidePanel?.setPanelBehavior) return;

  void chrome.sidePanel
    .setPanelBehavior({ openPanelOnActionClick: true })
    .catch((error) => console.error('Failed to configure side panel behavior', error));
});
