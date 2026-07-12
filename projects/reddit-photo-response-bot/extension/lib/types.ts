export type RelevanceLabel =
  | 'strong_match'
  | 'possible_match'
  | 'not_match'
  | 'skip_vendor_risk';

export type OwnerDecision = 'unreviewed' | 'relevant' | 'irrelevant' | 'hidden';

export interface ClassificationResult {
  label: RelevanceLabel;
  score: number;
  matchedSignals: string[];
  reason: string;
}

export interface DetectedPost {
  id: string;
  title: string;
  body: string;
  permalink: string;
  subreddit: string;
  detectedAt: string;
  classification: ClassificationResult;
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
