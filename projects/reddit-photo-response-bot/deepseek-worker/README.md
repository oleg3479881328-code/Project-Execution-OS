# WedditNYC DeepSeek Analysis Worker

Cloudflare Worker proxy for the Chrome side panel's second-stage semantic analysis.

## Security boundary

- `DEEPSEEK_API_KEY` is a Cloudflare Worker secret.
- `EXTENSION_ACCESS_KEY` is a separate random secret used by the extension to call this Worker.
- Neither secret is committed to Git.
- The extension never receives the DeepSeek API key.
- The Worker does not intentionally log post content or authorization headers.
- Requests and responses use `Cache-Control: no-store`.

## What the Worker sends to DeepSeek

Only when AI analysis is requested:

- subreddit name;
- post title;
- post body;
- post permalink;
- local rule-based classification.

It does not send Reddit credentials, cookies, browser history, or the owner's identity.

## Local checks

Requirements: Node.js 20+ and npm.

```bash
npm install
npm run check
```

For local development, create an uncommitted `.dev.vars` file:

```env
DEEPSEEK_API_KEY=your_real_deepseek_key
EXTENSION_ACCESS_KEY=a_separate_long_random_value
```

Then run:

```bash
npm run dev
```

Never paste real secrets into GitHub issues, pull requests, source files, or chat.

## Deploy to Cloudflare

```bash
npm install
npx wrangler login
npx wrangler secret put DEEPSEEK_API_KEY
npx wrangler secret put EXTENSION_ACCESS_KEY
npm run deploy
```

Wrangler will return a URL similar to:

```text
https://wedditnyc-deepseek-analysis.<account-subdomain>.workers.dev
```

## Connect the Chrome side panel

1. Open the extension's side panel.
2. Expand `DeepSeek semantic analysis`.
3. Enable the AI stage.
4. Paste the Worker URL.
5. Enter the separate `EXTENSION_ACCESS_KEY` value — not the DeepSeek API key.
6. Save settings and approve Chrome access only for that Worker origin.
7. Use `Analyze with AI` for one post or `AI analyze new candidates` for local Strong/Possible posts.

Automatic analysis is optional and disabled by default to control API usage.

## DeepSeek request mode

The Worker uses:

- endpoint: `https://api.deepseek.com/chat/completions`;
- model: `deepseek-v4-flash` by default;
- thinking mode: disabled;
- JSON output mode;
- low temperature for repeatability.

The model can be changed by updating `DEEPSEEK_MODEL` in `wrangler.toml`, followed by validation and redeployment.

## Production follow-up

Before broad public use, add Cloudflare rate limiting and replace the single shared extension access key with user-specific authentication. The current design is intended for one owner's internal extension.