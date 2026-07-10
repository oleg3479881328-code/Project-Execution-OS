import { browser } from 'wxt/browser';
import { median } from './analytics';
import { mergeVideoRecords } from './tiktok-parser';
import type { DashboardData, ProfileSnapshot, ScanState, VideoRecord } from './types';

const STORAGE_KEY = 'tiktokResearchSorter.dashboard.v1';

const initialState: DashboardData = {
  profiles: {},
  activeScan: {
    status: 'idle',
    videosFound: 0,
    updatedAt: Date.now(),
  },
};

export async function loadDashboard(): Promise<DashboardData> {
  const stored = await browser.storage.local.get(STORAGE_KEY);
  const value = stored[STORAGE_KEY] as DashboardData | undefined;
  return value ?? structuredClone(initialState);
}

export async function saveDashboard(data: DashboardData): Promise<void> {
  await browser.storage.local.set({ [STORAGE_KEY]: data });
}

export async function updateScanState(state: ScanState): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  dashboard.activeScan = state;
  await saveDashboard(dashboard);
  return dashboard;
}

export async function mergeVideoBatch(username: string, profileUrl: string, videos: VideoRecord[]): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  const existing: ProfileSnapshot = dashboard.profiles[username] ?? {
    username,
    profileUrl,
    videos: [],
    medianViews: 0,
    lastScannedAt: Date.now(),
  };
  const merged = new Map(existing.videos.map((video) => [video.id, video]));

  for (const incoming of videos) {
    const current = merged.get(incoming.id);
    merged.set(incoming.id, current ? mergeVideoRecords(current, incoming) : incoming);
  }

  existing.videos = [...merged.values()];
  existing.medianViews = median(existing.videos.map((video) => video.views).filter((value) => value > 0));
  existing.lastScannedAt = Date.now();
  dashboard.profiles[username] = existing;
  dashboard.activeScan.videosFound = existing.videos.length;
  dashboard.activeScan.updatedAt = Date.now();
  await saveDashboard(dashboard);
  return dashboard;
}

export async function clearProfile(username: string): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  delete dashboard.profiles[username];
  await saveDashboard(dashboard);
  return dashboard;
}
