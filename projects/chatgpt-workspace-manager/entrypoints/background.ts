import { browser, defineBackground } from '#imports';

export default defineBackground(() => {
  if (browser.sidePanel?.setPanelBehavior) {
    browser.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch((error) => {
      console.warn('[CWM] Unable to configure side panel behavior', error);
    });
  }
});
