export type ScanStatus = 'idle' | 'scanning' | 'paused' | 'complete' | 'stopped' | 'blocked' | 'error';

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

export interface ProfileSnapshot {
  username: string;
  profileUrl: string;
  displayName?: string;
  videos: VideoRecord[];
  medianViews: number;
  lastScannedAt: number;
}

export interface ScanState {
  status: ScanStatus;
  username?: string;
  profileUrl?: string;
  videosFound: number;
  startedAt?: number;
  updatedAt: number;
  oldestPublishedAt?: number;
  message?: string;
}

export interface ScanOptions {
  maxVideos: number;
  maxIdleRounds: number;
  scrollDelayMs: number;
}

export type RuntimeMessage =
  | { type: 'START_SCAN'; options: ScanOptions }
  | { type: 'STOP_SCAN' }
  | { type: 'GET_DASHBOARD' }
  | { type: 'CLEAR_PROFILE'; username: string }
  | { type: 'VIDEO_BATCH'; username: string; profileUrl: string; videos: VideoRecord[] }
  | { type: 'SCAN_STATE'; state: ScanState };

export interface DashboardData {
  profiles: Record<string, ProfileSnapshot>;
  activeScan: ScanState;
}
