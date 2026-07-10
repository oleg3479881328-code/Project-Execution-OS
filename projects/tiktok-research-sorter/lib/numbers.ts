const multipliers: Record<string, number> = {
  K: 1_000,
  M: 1_000_000,
  B: 1_000_000_000,
};

export function parseCompactNumber(input: unknown): number {
  if (typeof input === 'number') return Number.isFinite(input) ? Math.max(0, Math.round(input)) : 0;
  if (typeof input !== 'string') return 0;

  const normalized = input.trim().toUpperCase().replace(/\s/g, '').replace(/,/g, '');
  if (!normalized) return 0;

  const match = normalized.match(/^(-?\d+(?:\.\d+)?)([KMB])?$/);
  if (!match) {
    const digits = normalized.replace(/[^\d.-]/g, '');
    const fallback = Number(digits);
    return Number.isFinite(fallback) ? Math.max(0, Math.round(fallback)) : 0;
  }

  const value = Number(match[1]);
  const multiplier = match[2] ? multipliers[match[2]] ?? 1 : 1;
  return Number.isFinite(value) ? Math.max(0, Math.round(value * multiplier)) : 0;
}

export function formatCompactNumber(value: number): string {
  return new Intl.NumberFormat('ru-RU', {
    notation: 'compact',
    maximumFractionDigits: 1,
  }).format(value || 0);
}
