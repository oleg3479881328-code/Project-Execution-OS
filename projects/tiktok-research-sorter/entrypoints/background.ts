import { browser } from 'wxt/browser';
import { clearProfile, loadDashboard, mergeVideoBatch, updateScanState } from '../lib/store';
import type { RuntimeMessage } from '../lib/types';

export default defineBackground(() => {
  browser.sidePanel?.setPanelBehavior({ openPanelOnActionClick: true }).catch(() => undefined);

  browser.runtime.onMessage.addListener((message: RuntimeMessage) => {
    switch (message.type) {
      case 'GET_DASHBOARD':
        return loadDashboard();
      case 'VIDEO_BATCH':
        return mergeVideoBatch(message.username, message.profileUrl, message.videos).then((dashboard) => {
          void browser.runtime.sendMessage({ type: 'DASHBOARD_UPDATED', dashboard }).catch(() => undefined);
          return dashboard;
        });
      case 'SCAN_STATE':
        return updateScanState(message.state).then((dashboard) => {
          void browser.runtime.sendMessage({ type: 'DASHBOARD_UPDATED', dashboard }).catch(() => undefined);
          return dashboard;
        });
      case 'CLEAR_PROFILE':
        return clearProfile(message.username).then((dashboard) => {
          void browser.runtime.sendMessage({ type: 'DASHBOARD_UPDATED', dashboard }).catch(() => undefined);
          return dashboard;
        });
      default:
        return undefined;
    }
  });
});
