import { describe, expect, it } from 'vitest';
import { parseSemanticAnalysis } from '../src/schema';

describe('parseSemanticAnalysis', () => {
  it('normalizes a valid model response', () => {
    expect(
      parseSemanticAnalysis({
        label: 'possible_match',
        confidence: 81.7,
        customerIntent: 'Comparing photography prices',
        responseRisk: 'medium',
        reason: 'Photography is discussed, but active hiring is not explicit.',
        recommendedAction: 'review'
      })
    ).toEqual({
      label: 'possible_match',
      confidence: 82,
      customerIntent: 'Comparing photography prices',
      responseRisk: 'medium',
      reason: 'Photography is discussed, but active hiring is not explicit.',
      recommendedAction: 'review'
    });
  });

  it('rejects unknown labels and actions', () => {
    expect(() =>
      parseSemanticAnalysis({
        label: 'lead',
        confidence: 90,
        customerIntent: 'Unknown',
        responseRisk: 'low',
        reason: 'Unknown',
        recommendedAction: 'auto_comment'
      })
    ).toThrow();
  });
});