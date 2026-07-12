import type { ClassificationResult } from './types';

interface SignalRule {
  id: string;
  pattern: RegExp;
  weight: number;
}

const RISK_RULES: SignalRule[] = [
  { id: 'no-vendors', pattern: /\b(no|not accepting|please no)\s+vendors?\b/i, weight: -100 },
  { id: 'do-not-dm', pattern: /\b(do not|don'?t)\s+(dm|message|contact)\b/i, weight: -80 },
  { id: 'already-booked', pattern: /\b(already|have)\s+(booked|hired|found)\s+(a|our|my)?\s*photographer\b/i, weight: -70 },
  { id: 'not-looking', pattern: /\bnot\s+looking\s+for\s+(a\s+)?photographer\b/i, weight: -100 }
];

const STRONG_RULES: SignalRule[] = [
  { id: 'looking-for-photographer', pattern: /\b(looking|searching|seeking)\s+for\s+(a\s+)?(?:wedding\s+|engagement\s+|elopement\s+|city\s+hall\s+)?photographer\b/i, weight: 55 },
  { id: 'need-photographer', pattern: /\bneed\s+(a\s+)?(?:wedding\s+|engagement\s+|elopement\s+|city\s+hall\s+)?photographer\b/i, weight: 50 },
  { id: 'recommend-photographer', pattern: /\b(photographer\s+recommendations?|recommend(?:ation)?s?\s+for\s+(a\s+)?photographer|recommend\s+(a\s+)?(?:wedding\s+)?photographer)\b/i, weight: 50 },
  { id: 'last-minute-photographer', pattern: /\b(last[- ]minute|urgent).{0,30}\bphotographer\b/i, weight: 45 },
  { id: 'availability-request', pattern: /\bphotographer\b.{0,50}\b(available|availability|open date)\b/i, weight: 40 }
];

const POSSIBLE_RULES: SignalRule[] = [
  { id: 'wedding-photography', pattern: /\bwedding\s+photograph(?:er|y)\b/i, weight: 25 },
  { id: 'engagement-photography', pattern: /\bengagement\s+(?:shoot|session|photograph(?:er|y))\b/i, weight: 25 },
  { id: 'city-hall-photo', pattern: /\bcity\s+hall\b.{0,40}\b(photo|photographer|photography)\b/i, weight: 25 },
  { id: 'elopement-photo', pattern: /\belopement\b.{0,40}\b(photo|photographer|photography)\b/i, weight: 25 },
  { id: 'style-request', pattern: /\b(documentary|candid|editorial|photojournalistic)\b.{0,50}\b(photo|photographer|photography)\b/i, weight: 20 },
  { id: 'photo-budget', pattern: /\b(photo|photographer|photography)\b.{0,50}\b(budget|price|pricing|cost|quote|package)\b/i, weight: 20 },
  { id: 'generic-photographer', pattern: /\bphotographer\b/i, weight: 10 }
];

const UNRELATED_VENDOR_RULES: SignalRule[] = [
  { id: 'florist-only', pattern: /\b(looking|need|recommend).{0,30}\bflorist\b/i, weight: -20 },
  { id: 'venue-only', pattern: /\b(looking|need|recommend).{0,30}\bvenue\b/i, weight: -20 },
  { id: 'makeup-only', pattern: /\b(looking|need|recommend).{0,30}\b(makeup|mua|hair stylist)\b/i, weight: -20 },
  { id: 'catering-only', pattern: /\b(looking|need|recommend).{0,30}\b(caterer|catering)\b/i, weight: -20 },
  { id: 'dj-only', pattern: /\b(looking|need|recommend).{0,30}\b(dj|band|music)\b/i, weight: -20 },
  { id: 'officiant-only', pattern: /\b(looking|need|recommend).{0,30}\bofficiant\b/i, weight: -20 }
];

function collectMatches(text: string, rules: SignalRule[]): SignalRule[] {
  return rules.filter((rule) => rule.pattern.test(text));
}

export function classifyPost(title: string, body = ''): ClassificationResult {
  const text = `${title}\n${body}`.trim();
  const risks = collectMatches(text, RISK_RULES);

  if (risks.length > 0) {
    return {
      label: 'skip_vendor_risk',
      score: Math.max(-100, risks.reduce((sum, rule) => sum + rule.weight, 0)),
      matchedSignals: risks.map((rule) => rule.id),
      reason: `Vendor-response risk: ${risks.map((rule) => rule.id).join(', ')}`
    };
  }

  const strong = collectMatches(text, STRONG_RULES);
  const possible = collectMatches(text, POSSIBLE_RULES);
  const unrelated = collectMatches(text, UNRELATED_VENDOR_RULES);
  const matched = [...strong, ...possible, ...unrelated];
  const score = matched.reduce((sum, rule) => sum + rule.weight, 0);
  const matchedSignals = matched.map((rule) => rule.id);

  if (strong.length > 0 || score >= 45) {
    return {
      label: 'strong_match',
      score,
      matchedSignals,
      reason: `Clear photography intent: ${[...strong, ...possible]
        .map((rule) => rule.id)
        .join(', ')}`
    };
  }

  if (possible.length > 0 && score >= 10) {
    return {
      label: 'possible_match',
      score,
      matchedSignals,
      reason: `Photography is relevant, but intent needs review: ${possible
        .map((rule) => rule.id)
        .join(', ')}`
    };
  }

  return {
    label: 'not_match',
    score,
    matchedSignals,
    reason:
      unrelated.length > 0
        ? `Request appears focused on another vendor: ${unrelated
            .map((rule) => rule.id)
            .join(', ')}`
        : 'No meaningful wedding-photography request detected.'
  };
}
