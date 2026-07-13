import { browser } from 'wxt/browser';
import type {
  AiAnalysisResult,
  AiSettings,
  DetectedPost,
  OwnerDecision,
  RelevanceLabel
} from './types';

export const POSTS_STORAGE_KEY = 'redditPhotoResponseBot.posts.v1';
export const AI_SETTINGS_STORAGE_KEY = 'redditPhotoResponseBot.aiSettings.v1';

export const DEFAULT_AI_SETTINGS: AiSettings = {
  enabled: false,
  autoAnalyzeCandidates: false,
  proxyUrl: '',
  accessKey: ''
};

export async function listStoredPosts(): Promise<DetectedPost[]> {
  const result = await browser.storage.local.get(POSTS_STORAGE_KEY);
  const posts = result[POSTS_STORAGE_KEY] as Record<string, DetectedPost> | undefined;
  return Object.values(posts ?? {}).sort((a, b) =>
    b.detectedAt.localeCompare(a.detectedAt)
  );
}

export async function getStoredPost(id: string): Promise<DetectedPost | undefined> {
  const posts = await listStoredPosts();
  return posts.find((post) => post.id === id);
}

export async function upsertDetectedPost(post: DetectedPost): Promise<DetectedPost> {
  const result = await browser.storage.local.get(POSTS_STORAGE_KEY);
  const posts = (result[POSTS_STORAGE_KEY] as Record<string, DetectedPost> | undefined) ?? {};
  const existing = posts[post.id];
  const merged: DetectedPost = {
    ...post,
    aiAnalysis: existing?.aiAnalysis,
    aiError: existing?.aiError,
    manualLabel: existing?.manualLabel,
    ownerDecision: existing?.ownerDecision ?? post.ownerDecision,
    detectedAt: existing?.detectedAt ?? post.detectedAt
  };

  posts[post.id] = merged;
  await browser.storage.local.set({ [POSTS_STORAGE_KEY]: posts });
  return merged;
}

async function updateStoredPost(
  id: string,
  changes: Partial<DetectedPost>
): Promise<DetectedPost | undefined> {
  const result = await browser.storage.local.get(POSTS_STORAGE_KEY);
  const posts = (result[POSTS_STORAGE_KEY] as Record<string, DetectedPost> | undefined) ?? {};
  const current = posts[id];
  if (!current) return undefined;

  const next = { ...current, ...changes };
  posts[id] = next;
  await browser.storage.local.set({ [POSTS_STORAGE_KEY]: posts });
  return next;
}

export async function updatePostDecision(
  id: string,
  changes: { ownerDecision?: OwnerDecision; manualLabel?: RelevanceLabel }
): Promise<DetectedPost | undefined> {
  return updateStoredPost(id, changes);
}

export async function updatePostAiAnalysis(
  id: string,
  aiAnalysis: AiAnalysisResult | undefined,
  aiError?: string
): Promise<DetectedPost | undefined> {
  return updateStoredPost(id, { aiAnalysis, aiError });
}

export async function getAiSettings(): Promise<AiSettings> {
  const result = await browser.storage.local.get(AI_SETTINGS_STORAGE_KEY);
  return {
    ...DEFAULT_AI_SETTINGS,
    ...((result[AI_SETTINGS_STORAGE_KEY] as Partial<AiSettings> | undefined) ?? {})
  };
}

export async function saveAiSettings(settings: AiSettings): Promise<void> {
  await browser.storage.local.set({ [AI_SETTINGS_STORAGE_KEY]: settings });
}

export async function clearHiddenPosts(): Promise<number> {
  const result = await browser.storage.local.get(POSTS_STORAGE_KEY);
  const posts = (result[POSTS_STORAGE_KEY] as Record<string, DetectedPost> | undefined) ?? {};
  let removed = 0;

  for (const [id, post] of Object.entries(posts)) {
    if (post.ownerDecision === 'hidden') {
      delete posts[id];
      removed += 1;
    }
  }

  await browser.storage.local.set({ [POSTS_STORAGE_KEY]: posts });
  return removed;
}