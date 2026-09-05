# Pattern — X Ranking Engagement Signal Interpretation (2026-09)

## Status

candidate

## Captured

2026-09-05

## Type

pattern / researched platform-ranking reference

## Source / Evidence

Primary source: official open-source X ranking repository:

- `xai-org/x-algorithm`
- `home-mixer/params/param.rs`
- https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs

Observed social-media trigger: Facebook post by Aleko Sokurashvili claiming that X had published real ranking weights and interpreting them as raw count equivalences such as one report cancelling hundreds of likes.

The official source inspected on 2026-09-05 states that these weights multiply predicted probabilities of actions, not raw engagement counts, and explicitly calls the statement `one report cancels 468 likes` incorrect.

The inspected file also states it was mirrored from feature-switch defaults with last sync `2026-09-04T16:22:24Z`.

## Verified Weights In The Inspected X Configuration

| Signal | Weight |
| --- | ---: |
| Favorite / Like | 0.5 |
| Reply | 5.0 |
| Retweet / Repost | 1.0 |
| Quote | 5.0 |
| Share | 2.0 |
| Share via DM | 5.0 |
| Share via copy link | 20.0 |
| Follow author | 4.0 |
| Not interested | -43.2 |
| Block author | -31.2 |
| Mute author | -58.8 |
| Report | -234.0 |

Other nearby inspected weights include photo expand `0.05`, video open `0.07`, click `0.4`, open link `0.2`, dwell `0.05`, and not-dwelled `-0.02`.

## Critical Interpretation Rule

Do **not** convert weight ratios into raw event-count equivalences.

The ranking logic uses approximately:

`score contribution = weight × predicted probability of action`

Therefore:

- `ReportWeight / FavoriteWeight = -468` does **not** mean one report literally cancels 468 likes;
- the weights reflect both ranking value and the typical rarity/propensity of each action;
- X notes that report probability is more than 1000× lower than like probability, so its larger absolute weight allows that rare predicted signal to matter;
- recommendations are personalized, so negative-feedback behavior does not automatically suppress a post uniformly for every user;
- X also notes that coordinated direct navigation to a post does not have the same recommendation-system effect as an action on a post served in Home Timeline.

## Reusable Marketing Pattern

For X content strategy, optimize less for passive likes alone and more for content that naturally causes high-intent actions such as:

- meaningful replies;
- quotes;
- direct-message shares;
- copied links;
- author follows.

The strongest practical signal in the inspected configuration is `Share via copy link = 20.0`, compared with `Favorite = 0.5`.

This supports a content-design principle:

> Create posts people want to send to a specific person, discuss, quote, save/share externally, or use as a reason to follow the author — not merely posts that collect lightweight likes.

This is a strategy implication from the published ranking configuration, not a guarantee of reach for any individual post.

## Applies To

- X / Twitter organic content strategy;
- social-media growth experiments;
- ranking-algorithm research;
- evaluation of claims about X engagement weights;
- content hooks and CTA design where share/reply intent matters.

## Triggers

Load this entry when:

- planning X content;
- comparing engagement actions on X;
- reviewing a claim about ranking weights;
- designing experiments around likes, replies, reposts, quotes, DMs, copied links, follows, mutes, blocks, reports, or `Not interested`.

## Do Not Load When

- analyzing Facebook, Instagram, TikTok, YouTube, Threads, LinkedIn, or another platform unless explicitly comparing them with X;
- treating the listed values as permanently fixed — X can change feature-switch defaults and ranking architecture.

## Risks / Validation

- These are configuration values from the open-source repository at the inspected date, not a promise that every production request, experiment bucket, user, surface, or future version uses the same values.
- The repository and defaults should be rechecked before high-stakes or current-date strategic decisions.
- Do not infer raw-count causal equivalence from coefficient ratios.

## Review Status

Evidence checked against the official X open-source repository on 2026-09-05. Preserved as a `candidate` reusable pattern, not promoted to a mandatory system standard.
