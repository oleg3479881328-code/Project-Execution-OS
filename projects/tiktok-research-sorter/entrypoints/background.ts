import { browser } from 'wxt/browser';
import { clearProfile, loadDashboard, mergeProfileData, mergeVideoBatch, updateScanState } from '../lib/store';
import type { DashboardData, RuntimeMessage } from '../lib/types';

export default defineBackground(() => {
  browser.sidePanel?.setPanelBehavior({ openPanelOnActionClick: true }).catch(() => undefined);

  let mutationQueue: Promise<void> = Promise.resolve();

  const enqueue = <T,>(operation: () => Promise<T>): Promise<T> => {
    const next = mutationQueue.then(operation, operation);
    mutationQueue = next.then(() => undefined, () => undefined);
    return next;
  };

  const publish = (operation: () => Promise<DashboardData>) => enqueue(operation).then((dashboard) => {
    void browser.runtime.sendMessage({ type: 'DASHBOARD_UPDATED', dashboard } satisfies RuntimeMessage).catch(() => undefined);
    return dashboard;
  });

  browser.runtime.onMessage.addListener((message: RuntimeMessage) => {
    switch (message.type) {
      case 'GET_DASHBOARD':
        return enqueue(loadDashboard);
      case 'PROFILE_DATA':
        return publish(() => mergeProfileData(message.profile));
      case 'VIDEO_BATCH':
        return publish(() => mergeVideoBatch(message.username, message.profileUrl, message.videos));
      case 'SCAN_STATE':
        return publish(() => updateScanState(message.state));
      case 'CLEAR_PROFILE':
        return publish(() => clearProfile(message.username));
      default:
        return undefined;
    }
  });
});
