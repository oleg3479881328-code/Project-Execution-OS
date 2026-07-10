import { browser } from 'wxt/browser';
import { clearProfile, loadDashboard, mergeProfileData, mergeVideoBatch, updateScanState } from '../lib/store';
import type { RuntimeMessage } from '../lib/types';

export default defineBackground(() => {
  browser.sidePanel?.setPanelBehavior({ openPanelOnActionClick: true }).catch(() => undefined);

  browser.runtime.onMessage.addListener((message: RuntimeMessage) => {
    const publish = <T,>(promise: Promise<T>) => promise.then((dashboard) => {
      void browser.runtime.sendMessage({ type: 'DASHBOARD_UPDATED', dashboard }).catch(() => undefined);
      return dashboard;
    });

    switch (message.type) {
      case 'GET_DASHBOARD':
        return loadDashboard();
      case 'PROFILE_DATA':
        return publish(mergeProfileData(message.profile));
      case 'VIDEO_BATCH':
        return publish(mergeVideoBatch(message.username, message.profileUrl, message.videos));
      case 'SCAN_STATE':
        return publish(updateScanState(message.state));
      case 'CLEAR_PROFILE':
        return publish(clearProfile(message.username));
      default:
        return undefined;
    }
  });
});
