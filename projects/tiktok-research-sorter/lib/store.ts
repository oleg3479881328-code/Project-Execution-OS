import { browser } from 'wxt/browser';
import { median } from './analytics';
import {
  channelSnapshotFromProfile,
  favoriteKey,
  mergeChannelSnapshots,
  minimalChannelSnapshot,
  normalizeFavoriteEntry,
  profileKey,
} from './favorites';
import { mergeDiscoveredVideos } from './tag-research';
import { mergeVideoRecords } from './tiktok-parser';
import type {
  DashboardData,
  FavoriteEntry,
  ProfileRecord,
  ProfileSnapshot,
  ScanOptions,
  ScanState,
  TagResearchSnapshot,
  VideoRecord,
} from './types';

const STORAGE_KEY = 'tiktokResearchSorter.dashboard.v1';
const STALE_SCAN_MS = 2 * 60 * 1000;

const initialState: DashboardData = {
  profiles: {},
  tagResearch: {},
  favorites: {},
  activeScan: {
    status: 'idle',
    videosFound: 0,
    updatedAt: Date.now(),
  },
};

const sourcePriority: Record<ProfileRecord['source'], number> = {
  dom: 1,
  'embedded-json': 2,
  api: 3,
};

function normalizeTagKey(tag: string): string {
  return tag.trim().replace(/^#/, '').toLowerCase();
}

function normalizeFavorites(favorites: Record<string, FavoriteEntry> | undefined): Record<string, FavoriteEntry> {
  if (!favorites) return {};
  return Object.fromEntries(
    Object.entries(favorites).map(([storedKey, entry]) => {
      const normalized = normalizeFavoriteEntry(entry as Partial<FavoriteEntry> & { video: VideoRecord });
      return [storedKey || normalized.key, normalized];
    }),
  );
}

function normalizeDashboard(value: Partial<DashboardData> | undefined): DashboardData {
  if (!value) return structuredClone(initialState);
  return {
    profiles: value.profiles ?? {},
    tagResearch: value.tagResearch ?? {},
    favorites: normalizeFavorites(value.favorites),
    activeScan: value.activeScan ?? structuredClone(initialState.activeScan),
  };
}

function findProfile(dashboard: DashboardData, username: string): ProfileSnapshot | undefined {
  const key = profileKey(username);
  return Object.values(dashboard.profiles).find((profile) => profileKey(profile.username) === key);
}

function refreshFavoriteChannels(dashboard: DashboardData, profile: ProfileSnapshot): void {
  const channel = channelSnapshotFromProfile(profile);
  const username = profileKey(profile.username);

  for (const [key, rawEntry] of Object.entries(dashboard.favorites)) {
    const entry = normalizeFavoriteEntry(rawEntry);
    if (profileKey(entry.video.author) !== username) continue;
    dashboard.favorites[key] = {
      ...entry,
      channel: mergeChannelSnapshots(entry.channel, channel),
    };
  }
}

export async function loadDashboard(): Promise<DashboardData> {
  const stored = await browser.storage.local.get(STORAGE_KEY);
  const dashboard = normalizeDashboard(stored[STORAGE_KEY] as Partial<DashboardData> | undefined);

  if (
    dashboard.activeScan.status === 'scanning'
    && Date.now() - dashboard.activeScan.updatedAt > STALE_SCAN_MS
  ) {
    dashboard.activeScan = {
      ...dashboard.activeScan,
      status: 'error',
      updatedAt: Date.now(),
      message: 'Предыдущее сканирование было прервано. Запустите его снова.',
    };
    await saveDashboard(dashboard);
  }

  return dashboard;
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

function emptyProfile(username: string, profileUrl: string): ProfileSnapshot {
  return {
    username,
    profileUrl,
    videos: [],
    medianViews: 0,
    lastScannedAt: Date.now(),
  };
}

export async function mergeProfileData(profile: ProfileRecord): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  const existing = findProfile(dashboard, profile.username) ?? emptyProfile(profile.username, profile.profileUrl);
  const existingPriority = existing.profileDataSource ? sourcePriority[existing.profileDataSource] : 0;
  const incomingPriority = sourcePriority[profile.source];
  const canReplace = incomingPriority >= existingPriority;

  const choose = <T,>(incoming: T | undefined, current: T | undefined): T | undefined => {
    if (canReplace) return incoming ?? current;
    return current ?? incoming;
  };

  const mergedProfile: ProfileSnapshot = {
    ...existing,
    username: choose(profile.username, existing.username) ?? existing.username,
    profileUrl: choose(profile.profileUrl, existing.profileUrl) ?? existing.profileUrl,
    userId: choose(profile.userId, existing.userId),
    secUid: choose(profile.secUid, existing.secUid),
    displayName: choose(profile.displayName, existing.displayName),
    bio: choose(profile.bio, existing.bio),
    avatarUrl: choose(profile.avatarUrl, existing.avatarUrl),
    followers: choose(profile.followers, existing.followers),
    following: choose(profile.following, existing.following),
    friends: choose(profile.friends, existing.friends),
    totalLikes: choose(profile.totalLikes, existing.totalLikes),
    videoCount: choose(profile.videoCount, existing.videoCount),
    verified: choose(profile.verified, existing.verified),
    privateAccount: choose(profile.privateAccount, existing.privateAccount),
    commerceAccount: choose(profile.commerceAccount, existing.commerceAccount),
    website: choose(profile.website, existing.website),
    region: choose(profile.region, existing.region),
    language: choose(profile.language, existing.language),
    accountCreatedAt: choose(profile.accountCreatedAt, existing.accountCreatedAt),
    profileDataUpdatedAt: Math.max(profile.collectedAt, existing.profileDataUpdatedAt ?? 0),
    profileDataSource: canReplace || !existing.profileDataSource ? profile.source : existing.profileDataSource,
  };

  delete dashboard.profiles[existing.username];
  dashboard.profiles[mergedProfile.username] = mergedProfile;
  refreshFavoriteChannels(dashboard, mergedProfile);

  await saveDashboard(dashboard);
  return dashboard;
}

export async function mergeVideoBatch(username: string, profileUrl: string, videos: VideoRecord[]): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  const existing = findProfile(dashboard, username) ?? emptyProfile(username, profileUrl);
  const merged = new Map(existing.videos.map((video) => [video.id, video]));

  for (const incoming of videos) {
    const current = merged.get(incoming.id);
    merged.set(incoming.id, current ? mergeVideoRecords(current, incoming) : incoming);
  }

  existing.videos = [...merged.values()];
  existing.medianViews = median(existing.videos.map((video) => video.views).filter((value) => value > 0));
  existing.lastScannedAt = Date.now();
  dashboard.profiles[existing.username] = existing;
  refreshFavoriteChannels(dashboard, existing);
  dashboard.activeScan.videosFound = existing.videos.length;
  dashboard.activeScan.updatedAt = Date.now();
  await saveDashboard(dashboard);
  return dashboard;
}

export async function beginTagResearch(
  tag: string,
  tagUrl: string,
  options: ScanOptions,
): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  const key = normalizeTagKey(tag);
  dashboard.tagResearch[key] = {
    tag: key,
    tagUrl,
    videos: [],
    topVideosPerAccount: Math.max(1, Math.floor(options.topVideosPerAccount)),
    minViews: Math.max(0, Math.floor(options.minViews)),
    scannedVideos: 0,
    accountsFound: 0,
    lastScannedAt: Date.now(),
  };
  await saveDashboard(dashboard);
  return dashboard;
}

export async function mergeTagVideoBatch(
  tag: string,
  tagUrl: string,
  videos: VideoRecord[],
): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  const key = normalizeTagKey(tag);
  const existing: TagResearchSnapshot = dashboard.tagResearch[key] ?? {
    tag: key,
    tagUrl,
    videos: [],
    topVideosPerAccount: 1,
    minViews: 0,
    scannedVideos: 0,
    accountsFound: 0,
    lastScannedAt: Date.now(),
  };

  existing.videos = mergeDiscoveredVideos([...existing.videos, ...videos]);
  existing.scannedVideos = existing.videos.length;
  existing.accountsFound = new Set(existing.videos.map((video) => video.author.toLowerCase())).size;
  existing.lastScannedAt = Date.now();
  existing.tagUrl = tagUrl;
  dashboard.tagResearch[key] = existing;
  dashboard.activeScan.videosFound = existing.scannedVideos;
  dashboard.activeScan.accountsFound = existing.accountsFound;
  dashboard.activeScan.updatedAt = Date.now();
  await saveDashboard(dashboard);
  return dashboard;
}

export async function toggleFavorite(video: VideoRecord): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  const key = favoriteKey(video);

  if (dashboard.favorites[key]) {
    delete dashboard.favorites[key];
  } else {
    const profile = findProfile(dashboard, video.author);
    dashboard.favorites[key] = {
      key,
      video: structuredClone(video),
      channel: profile ? channelSnapshotFromProfile(profile) : minimalChannelSnapshot(video),
      favoritedAt: Date.now(),
    };
  }

  await saveDashboard(dashboard);
  return dashboard;
}

export async function removeFavorites(keys: string[]): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  for (const key of new Set(keys)) delete dashboard.favorites[key];
  await saveDashboard(dashboard);
  return dashboard;
}

export async function clearProfile(username: string): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  const profile = findProfile(dashboard, username);
  if (profile) delete dashboard.profiles[profile.username];
  await saveDashboard(dashboard);
  return dashboard;
}

export async function clearTagResearch(tag: string): Promise<DashboardData> {
  const dashboard = await loadDashboard();
  delete dashboard.tagResearch[normalizeTagKey(tag)];
  await saveDashboard(dashboard);
  return dashboard;
}
