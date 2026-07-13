export type RelevanceLabel =
  | 'strong_match'
  | 'possible_match'
  | 'not_match'
  | 'skip_vendor_risk';

export type OwnerDecision = 'unreviewed' | 'relevant' | 'irrelevant' | 'hidden';
export type AiResponseRisk = 'low' | 'medium' | 'high';
export type AiRecommendedAction = 'respond' | 'review' | 'skip';

export interface ClassificationResult {
  label: RelevanceLabel;
  score: number;
  matchedSignals: string[];
  reason: string;
}

export interface AiAnalysisResult {
  label: RelevanceLabel;
  confidence: number;
  customerIntent: string;
  responseRisk: AiResponseRisk;
  reason: string;
  recommendedAction: AiRecommendedAction;
  analyzedAt: string;
  model: string;
}

export interface AiSettings {
  enabled: boolean;
  autoAnalyzeCandidates: boolean;
  proxyUrl: string;
  accessKey: string;
}

export interface DetectedPost {
  id: string;
  title: string;
  body: string;
  permalink: string;
  subreddit: string;
  detectedAt: string;
  classification: ClassificationResult;
  aiAnalysis?: AiAnalysisResult;
  aiError?: string;
  manualLabel?: RelevanceLabel;
  ownerDecision: OwnerDecision;
}

export interface ParsedRedditPost {
  id: string;
  title: string;
  body: string;
  permalink: string;
  subreddit: string;
}