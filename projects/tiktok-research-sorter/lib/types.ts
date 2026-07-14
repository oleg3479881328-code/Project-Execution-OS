export const APP_VERSION = '0.4.0';

export type ScanStatus = 'idle' | 'scanning' | 'paused' | 'complete' | 'stopped' | 'blocked' | 'error';
export type ScanMode = 'profile' | 'tag';

export interface ProfilePageContext {
  kind: 'profile';
  username: string;
  profileUrl: string;
}

export interface TagPageContext {
  kind: 'tag';
  tag: string;
  tagUrl: string;
}

export type TikTokPageContext = ProfilePageContext | TagPageContext;

export interface VideoRecord {
  id: string;
  author: string;
  profileUrl: string;
  videoUrl: string;
  description: string;
  publishedAt?: number;
  durationSeconds?: number;
  views: number;
  likes: number;
  comments: number;
  shares: number;
  saves?: number;
  coverUrl?: string;
  hashtags: string[];
  audioTitle?: string;
  isPinned: boolean;
  collectedAt: number;
  source: 'api' | 'embedded-json' | 'dom';
}

export interface EnrichedVideo extends VideoRecord {
  ageDays?: number;
  viewsPerDay?: number;
  engagementRate?: number;
  likeRate?: number;
  commentRate?: number;
  shareRate?: number;
  outlierScore?: number;
}

export interface FavoriteEntry {
  key: string;
  video: VideoRecord;
  favoritedAt: number;
}

export interface ProfileRecord {
  username: string;
  profileUrl: string;
  displayName?: string;
  bio?: string;
  avatarUrl?: string;
  followers?: number;
  following?: number;
  totalLikes?: number;
  videoCount?: number;
  verified?: boolean;
  website?: string;
  collectedAt: number;
  source: 'api' | 'embedded-json' | 'dom';
}

export interface ProfileSnapshot extends Omit<ProfileRecord, 'collectedAt' | 'source'> {
  videos: VideoRecord[];
  medianViews: number;
  lastScannedAt: number;
  profileDataUpdatedAt?: number;
  profileDataSource?: ProfileRecord['source'];
}

export interface ScanOptions {
  maxVideos: number;
  maxIdleRounds: number;
  scrollDelayMs: number;
  topVideosPerAccount: number;
  minViews: number;
}

export interface TagResearchSnapshot {
  tag: string;
  tagUrl: string;
  videos: VideoRecord[];
  topVideosPerAccount: number;
  minViews: number;
  scannedVideos: number;
  accountsFound: number;
  lastScannedAt: number;
}

export interface ScanState {
  status: ScanStatus;
  mode?: ScanMode;
  username?: string;
  profileUrl?: string;
  tag?: string;
  tagUrl?: string;
  videosFound: number;
  accountsFound?: number;
  startedAt?: number;
  updatedAt: number;
  oldestPublishedAt?: number;
  message?: string;
}

export type RuntimeMessage =
  | { type: 'PING' }
  | { type: 'START_SCAN'; options: ScanOptions }
  | { type: 'STOP_SCAN' }
  | { type: 'GET_DASHBOARD' }
  | { type: 'CLEAR_PROFILE'; username: string }
  | { type: 'CLEAR_TAG_RESEARCH'; tag: string }
  | { type: 'TOGGLE_FAVORITE'; video: VideoRecord }
  | { type: 'REMOVE_FAVORITES'; keys: string[] }
  | { type: 'PROFILE_DATA'; profile: ProfileRecord }
  | { type: 'VIDEO_BATCH'; username: string; profileUrl: string; videos: VideoRecord[] }
  | { type: 'TAG_SCAN_BEGIN'; tag: string; tagUrl: string; options: ScanOptions }
  | { type: 'TAG_VIDEO_BATCH'; tag: string; tagUrl: string; videos: VideoRecord[] }
  | { type: 'SCAN_STATE'; state: ScanState }
  | { type: 'DASHBOARD_UPDATED'; dashboard: DashboardData };

export interface DashboardData {
  profiles: Record<string, ProfileSnapshot>;
  tagResearch: Record<string, TagResearchSnapshot>;
  favorites: Record<string, FavoriteEntry>;
  activeScan: ScanState;
}
