import { browser } from 'wxt/browser';
import type {
  AiAnalysisResult,
  AiRecommendedAction,
  AiResponseRisk,
  AiSettings,
  DetectedPost,
  RelevanceLabel
} from './types';

const LABELS: RelevanceLabel[] = [
  'strong_match',
  'possible_match',
  'not_match',
  'skip_vendor_risk'
];
const RISKS: AiResponseRisk[] = ['low', 'medium', 'high'];
const ACTIONS: AiRecommendedAction[] = ['respond', 'review', 'skip'];

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

export function parseAiAnalysis(value: unknown): AiAnalysisResult {
  if (!isRecord(value)) throw new Error('AI proxy returned a non-object response.');

  const label = value.label;
  const confidence = value.confidence;
  const customerIntent = value.customerIntent;
  const responseRisk = value.responseRisk;
  const reason = value.reason;
  const recommendedAction = value.recommendedAction;
  const analyzedAt = value.analyzedAt;
  const model = value.model;

  if (!LABELS.includes(label as RelevanceLabel)) throw new Error('Invalid AI label.');
  if (typeof confidence !== 'number' || confidence < 0 || confidence > 100) {
    throw new Error('Invalid AI confidence.');
  }
  if (typeof customerIntent !== 'string' || customerIntent.trim().length === 0) {
    throw new Error('Invalid AI customer intent.');
  }
  if (!RISKS.includes(responseRisk as AiResponseRisk)) throw new Error('Invalid AI risk.');
  if (typeof reason !== 'string' || reason.trim().length === 0) {
    throw new Error('Invalid AI reason.');
  }
  if (!ACTIONS.includes(recommendedAction as AiRecommendedAction)) {
    throw new Error('Invalid AI recommended action.');
  }
  if (typeof analyzedAt !== 'string' || Number.isNaN(Date.parse(analyzedAt))) {
    throw new Error('Invalid AI analysis timestamp.');
  }
  if (typeof model !== 'string' || model.trim().length === 0) {
    throw new Error('Invalid AI model.');
  }

  return {
    label: label as RelevanceLabel,
    confidence,
    customerIntent,
    responseRisk: responseRisk as AiResponseRisk,
    reason,
    recommendedAction: recommendedAction as AiRecommendedAction,
    analyzedAt,
    model
  };
}

export function isAiConfigured(settings: AiSettings): boolean {
  if (!settings.enabled || !settings.proxyUrl.trim() || !settings.accessKey.trim()) return false;
  try {
    return new URL(settings.proxyUrl).protocol === 'https:';
  } catch {
    return false;
  }
}

export async function requestProxyPermission(proxyUrl: string): Promise<boolean> {
  const url = new URL(proxyUrl);
  if (url.protocol !== 'https:') throw new Error('AI proxy URL must use HTTPS.');
  return browser.permissions.request({ origins: [`${url.origin}/*`] });
}

export async function analyzePostWithAi(
  post: DetectedPost,
  settings: AiSettings
): Promise<AiAnalysisResult> {
  if (!isAiConfigured(settings)) throw new Error('AI analysis is not configured.');

  const endpoint = `${settings.proxyUrl.replace(/\/+$/, '')}/analyze`;
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${settings.accessKey}`
    },
    body: JSON.stringify({
      post: {
        id: post.id,
        title: post.title,
        body: post.body,
        permalink: post.permalink,
        subreddit: post.subreddit
      },
      localClassification: post.classification
    })
  });

  const payload = (await response.json().catch(() => null)) as unknown;
  if (!response.ok) {
    const message = isRecord(payload) && typeof payload.error === 'string'
      ? payload.error
      : `AI proxy request failed with status ${response.status}.`;
    throw new Error(message);
  }

  return parseAiAnalysis(payload);
}