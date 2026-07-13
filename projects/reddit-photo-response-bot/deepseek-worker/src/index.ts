import { parseSemanticAnalysis } from './schema';

interface Env {
  DEEPSEEK_API_KEY: string;
  EXTENSION_ACCESS_KEY: string;
  DEEPSEEK_MODEL?: string;
}

interface AnalyzeRequest {
  post?: {
    id?: unknown;
    title?: unknown;
    body?: unknown;
    permalink?: unknown;
    subreddit?: unknown;
  };
  localClassification?: unknown;
}

const JSON_HEADERS = {
  'Content-Type': 'application/json; charset=utf-8',
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Authorization, Content-Type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS',
  'Cache-Control': 'no-store'
};

function json(value: unknown, status = 200): Response {
  return new Response(JSON.stringify(value), { status, headers: JSON_HEADERS });
}

function safeEqual(left: string, right: string): boolean {
  const encoder = new TextEncoder();
  const a = encoder.encode(left);
  const b = encoder.encode(right);
  let diff = a.length ^ b.length;
  const length = Math.max(a.length, b.length);
  for (let index = 0; index < length; index += 1) {
    diff |= (a[index] ?? 0) ^ (b[index] ?? 0);
  }
  return diff === 0;
}

function readString(value: unknown, maxLength: number): string {
  return typeof value === 'string' ? value.trim().slice(0, maxLength) : '';
}

function authorized(request: Request, env: Env): boolean {
  const header = request.headers.get('Authorization') ?? '';
  const token = header.startsWith('Bearer ') ? header.slice(7) : '';
  return Boolean(token && env.EXTENSION_ACCESS_KEY && safeEqual(token, env.EXTENSION_ACCESS_KEY));
}

function buildSystemPrompt(): string {
  return [
    'You classify Reddit wedding-planning posts for a legitimate wedding photographer.',
    'Determine whether the author is a potential photography client and whether a vendor response is appropriate.',
    'Do not write a reply to the Reddit user.',
    'Return one JSON object only with these exact camelCase keys:',
    'label, confidence, customerIntent, responseRisk, reason, recommendedAction.',
    'Allowed label values: strong_match, possible_match, not_match, skip_vendor_risk.',
    'Allowed responseRisk values: low, medium, high.',
    'Allowed recommendedAction values: respond, review, skip.',
    'confidence must be an integer from 0 to 100.',
    'Use skip_vendor_risk when the author rejects vendors, says not to DM/contact, already hired a photographer, or a promotional response would be clearly inappropriate.',
    'Use strong_match only when there is clear current intent to find, hire, compare, price, or request recommendations for a photographer.',
    'Use possible_match when photography is relevant but hiring intent is uncertain.',
    'Use not_match when the post is unrelated to hiring photography.',
    'Keep customerIntent and reason short, factual, and grounded only in the supplied post.'
  ].join('\n');
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: JSON_HEADERS });

    const url = new URL(request.url);
    if (request.method !== 'POST' || url.pathname !== '/analyze') {
      return json({ error: 'Not found.' }, 404);
    }
    if (!authorized(request, env)) return json({ error: 'Unauthorized.' }, 401);
    if (!env.DEEPSEEK_API_KEY) return json({ error: 'Worker is missing DeepSeek configuration.' }, 503);

    const contentLength = Number(request.headers.get('Content-Length') ?? '0');
    if (contentLength > 50_000) return json({ error: 'Request is too large.' }, 413);

    let input: AnalyzeRequest;
    try {
      input = (await request.json()) as AnalyzeRequest;
    } catch {
      return json({ error: 'Invalid JSON request.' }, 400);
    }

    const title = readString(input.post?.title, 1_000);
    const body = readString(input.post?.body, 12_000);
    const subreddit = readString(input.post?.subreddit, 100);
    const permalink = readString(input.post?.permalink, 2_000);
    if (!title) return json({ error: 'Post title is required.' }, 400);

    const model = env.DEEPSEEK_MODEL || 'deepseek-v4-flash';
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 30_000);

    try {
      const deepSeekResponse = await fetch('https://api.deepseek.com/chat/completions', {
        method: 'POST',
        signal: controller.signal,
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${env.DEEPSEEK_API_KEY}`
        },
        body: JSON.stringify({
          model,
          messages: [
            { role: 'system', content: buildSystemPrompt() },
            {
              role: 'user',
              content: JSON.stringify({
                subreddit,
                title,
                body,
                permalink,
                localClassification: input.localClassification ?? null
              })
            }
          ],
          thinking: { type: 'disabled' },
          response_format: { type: 'json_object' },
          temperature: 0.1,
          max_tokens: 700,
          stream: false
        })
      });

      if (!deepSeekResponse.ok) {
        return json({ error: `DeepSeek request failed with status ${deepSeekResponse.status}.` }, 502);
      }

      const completion = (await deepSeekResponse.json()) as {
        choices?: Array<{ message?: { content?: string | null } }>;
      };
      const content = completion.choices?.[0]?.message?.content;
      if (!content) return json({ error: 'DeepSeek returned an empty result.' }, 502);

      let parsed: unknown;
      try {
        parsed = JSON.parse(content);
      } catch {
        return json({ error: 'DeepSeek returned invalid JSON.' }, 502);
      }

      const analysis = parseSemanticAnalysis(parsed);
      return json({
        ...analysis,
        analyzedAt: new Date().toISOString(),
        model
      });
    } catch (error) {
      if (error instanceof Error && error.name === 'AbortError') {
        return json({ error: 'DeepSeek request timed out.' }, 504);
      }
      return json({ error: 'AI analysis failed.' }, 502);
    } finally {
      clearTimeout(timeout);
    }
  }
};