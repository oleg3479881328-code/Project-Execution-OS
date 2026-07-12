export type RelevanceLabel =
  | 'strong_match'
  | 'possible_match'
  | 'not_match'
  | 'skip_vendor_risk';
export type ResponseRisk = 'low' | 'medium' | 'high';
export type RecommendedAction = 'respond' | 'review' | 'skip';

export interface SemanticAnalysis {
  label: RelevanceLabel;
  confidence: number;
  customerIntent: string;
  responseRisk: ResponseRisk;
  reason: string;
  recommendedAction: RecommendedAction;
}

const LABELS: RelevanceLabel[] = [
  'strong_match',
  'possible_match',
  'not_match',
  'skip_vendor_risk'
];
const RISKS: ResponseRisk[] = ['low', 'medium', 'high'];
const ACTIONS: RecommendedAction[] = ['respond', 'review', 'skip'];

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === 'object' && value !== null && !Array.isArray(value);
}

function requiredString(record: Record<string, unknown>, key: string, max = 1000): string {
  const value = record[key];
  if (typeof value !== 'string' || value.trim().length === 0) {
    throw new Error(`DeepSeek output field ${key} must be a non-empty string.`);
  }
  return value.trim().slice(0, max);
}

export function parseSemanticAnalysis(value: unknown): SemanticAnalysis {
  if (!isRecord(value)) throw new Error('DeepSeek output must be a JSON object.');

  const label = value.label;
  const confidence = value.confidence;
  const responseRisk = value.responseRisk;
  const recommendedAction = value.recommendedAction;

  if (!LABELS.includes(label as RelevanceLabel)) throw new Error('Invalid label.');
  if (typeof confidence !== 'number' || !Number.isFinite(confidence)) {
    throw new Error('Invalid confidence.');
  }
  if (!RISKS.includes(responseRisk as ResponseRisk)) throw new Error('Invalid response risk.');
  if (!ACTIONS.includes(recommendedAction as RecommendedAction)) {
    throw new Error('Invalid recommended action.');
  }

  return {
    label: label as RelevanceLabel,
    confidence: Math.max(0, Math.min(100, Math.round(confidence))),
    customerIntent: requiredString(value, 'customerIntent', 500),
    responseRisk: responseRisk as ResponseRisk,
    reason: requiredString(value, 'reason', 1000),
    recommendedAction: recommendedAction as RecommendedAction
  };
}