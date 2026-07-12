const suffixes: Array<{ pattern: RegExp; multiplier: number }> = [
  { pattern: /млрд\.?$/u, multiplier: 1_000_000_000 },
  { pattern: /млн\.?$/u, multiplier: 1_000_000 },
  { pattern: /тыс\.?$/u, multiplier: 1_000 },
  { pattern: /b$/u, multiplier: 1_000_000_000 },
  { pattern: /m$/u, multiplier: 1_000_000 },
  { pattern: /k$/u, multiplier: 1_000 },
];

function normalizeNumericPart(input: string, compact: boolean): string | undefined {
  const value = input.replace(/[\s\u00a0\u202f']/gu, '');
  if (!/^[+-]?\d[\d.,]*$/u.test(value)) return undefined;

  const sign = value.startsWith('-') ? '-' : '';
  const unsigned = value.replace(/^[+-]/u, '');
  const commaCount = (unsigned.match(/,/gu) ?? []).length;
  const dotCount = (unsigned.match(/\./gu) ?? []).length;
  const lastComma = unsigned.lastIndexOf(',');
  const lastDot = unsigned.lastIndexOf('.');
  const lastSeparator = Math.max(lastComma, lastDot);

  if (lastSeparator < 0) return `${sign}${unsigned}`;

  const fractionalLength = unsigned.length - lastSeparator - 1;
  const separatorCount = commaCount + dotCount;
  const shouldTreatLastAsDecimal = compact
    ? fractionalLength > 0 && fractionalLength <= 3
    : separatorCount === 1 && fractionalLength !== 3;

  if (shouldTreatLastAsDecimal) {
    const integerPart = unsigned.slice(0, lastSeparator).replace(/[.,]/gu, '');
    const fractionPart = unsigned.slice(lastSeparator + 1).replace(/[.,]/gu, '');
    if (!integerPart || !fractionPart) return undefined;
    return `${sign}${integerPart}.${fractionPart}`;
  }

  if (commaCount > 0 && dotCount > 0) {
    const integerPart = unsigned.slice(0, lastSeparator).replace(/[.,]/gu, '');
    const fractionPart = unsigned.slice(lastSeparator + 1).replace(/[.,]/gu, '');
    if (fractionalLength > 0 && fractionalLength <= 2 && integerPart && fractionPart) {
      return `${sign}${integerPart}.${fractionPart}`;
    }
  }

  return `${sign}${unsigned.replace(/[.,]/gu, '')}`;
}

export function parseCompactNumber(input: unknown): number {
  if (typeof input === 'number') return Number.isFinite(input) ? Math.max(0, Math.round(input)) : 0;
  if (typeof input !== 'string') return 0;

  let normalized = input.trim().toLowerCase();
  if (!normalized) return 0;

  let multiplier = 1;
  for (const suffix of suffixes) {
    if (!suffix.pattern.test(normalized)) continue;
    multiplier = suffix.multiplier;
    normalized = normalized.replace(suffix.pattern, '');
    break;
  }

  const numericPart = normalizeNumericPart(normalized, multiplier !== 1);
  if (!numericPart) return 0;

  const value = Number(numericPart);
  return Number.isFinite(value) ? Math.max(0, Math.round(value * multiplier)) : 0;
}

export function formatCompactNumber(value: number): string {
  return new Intl.NumberFormat('ru-RU', {
    notation: 'compact',
    maximumFractionDigits: 1,
  }).format(value || 0);
}
