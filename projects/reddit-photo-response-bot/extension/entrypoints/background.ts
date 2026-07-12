type SidePanelApi = {
  setPanelBehavior(options: { openPanelOnActionClick: boolean }): Promise<void>;
};

type ChromeRuntime = {
  sidePanel?: SidePanelApi;
};

export default defineBackground(() => {
  const chromeRuntime = (globalThis as typeof globalThis & { chrome?: ChromeRuntime }).chrome;
  if (!chromeRuntime?.sidePanel) return;

  void chromeRuntime.sidePanel
    .setPanelBehavior({ openPanelOnActionClick: true })
    .catch((error: unknown) =>
      console.error('Failed to configure side panel behavior', error)
    );
});
