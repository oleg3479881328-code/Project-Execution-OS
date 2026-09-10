# Tusia / Tasha Hurley Weddings — Client Validation Pivot

## Date

2026-09-10

## Source

Direct conversation between Oleg and Tasha about SEO, the current staging concept, content quality, client workload and the practical next step.

## Classification

Project-specific durable decision and client-operating constraint.

Unrelated personal/family/payment conversation from the same call is intentionally excluded from this project log.

## What Tasha Confirmed

Tasha explicitly said that SEO is wanted and useful. She did **not** reject the SEO direction or the idea of adding wedding/venue content to her existing site.

Her objections were operational and qualitative:

- she does not want to abandon or rebuild her existing website;
- she does not want large amounts of obviously AI-written/generic copy that she then has to rewrite;
- the existing rough venue text looked like gibberish / obvious AI to her and did not demonstrate the result she wants;
- she needs a specific, very small next action from her rather than a broad explanation of the whole system;
- meaningful wedding content requires real inputs beyond only couple name + venue name;
- her own voice and real couple details matter;
- September and October are overloaded with weddings, gallery delivery and immediate client work;
- November is a better month for broader business/SEO optimization;
- she is willing to send material for one wedding now/earlier as a test without committing to a broad rollout.

## Agreed Minimal Client Input

Tasha proposed supplying one real wedding with three source groups:

1. the wedding gallery / photographs she wants considered;
2. an example of her own blog/page/block showing how she likes the content to look and/or read;
3. richer first-party wedding material, especially officiant/ceremony text, couple story, how they met, or similar personal details supplied by the couple.

This is now the canonical minimal client input for the first pilot.

## Decision

**One real wedding becomes the validation pilot. No broad content scaling until that pilot is approved.**

The system should take the three source groups and produce one complete, coherent real-wedding page inside Tasha's existing site experience.

Tasha should not be asked to manually create the SEO system, rewrite a pile of generated fragments, rename files, write alt text, build schema or define entity relationships.

## Content Rule

Generic AI-style wedding copy is not acceptable as the production default.

For the pilot:

- use Tasha's own writing/reference as the voice guide;
- use first-party wedding material for substantive details;
- do not invent facts;
- do not pad sparse evidence with decorative filler that reads as wedding-specific truth;
- AI may structure, edit, summarize and transform source material, but the public page should feel authored for Tasha and grounded in actual evidence.

## SEO / AEO Rule

SEO/AEO work remains important, but much of it should be invisible client burden handled under the hood.

Where supported, the system should handle:

- descriptive filenames;
- image alt text;
- metadata;
- structured data;
- venue/vendor/entity relationships;
- internal linking;
- useful location/venue context;
- search/AI-readable structure.

The human-facing page must not read like SEO scaffolding.

## Website Rule

Tasha's existing website remains the site shell.

Do not present the project as a platform migration or replacement site.

New venue/wedding pages must preserve/integrate with the existing navigation, transitions and overall site experience. Routine editing, especially swapping/removing photographs, should stay simple.

## Client Review Contract

The client review unit is **one finished preview**, not a bundle of disconnected AI drafts.

The first validation should answer:

- Does the voice feel like Tasha rather than generic AI?
- Is the page factually accurate and meaningful?
- Does it feel like part of her real site?
- Is the amount of client correction/review acceptably small?
- Does the SEO/AEO structure support rather than damage the human-facing experience?

Only after a positive answer should the pattern become reusable at scale.

## Timing / Engagement

September–October 2026:

- minimize required client participation;
- no broad optimization push;
- one pilot may proceed if Tasha sends the source bundle;
- do not repeatedly chase her for materials.

November 2026:

- preferred window for broader optimization and scaling, assuming pilot validation succeeds.

## Architecture Impact

Existing architecture remains valid:

`first-party sources / research -> identity resolution -> Knowledge DB -> SEO Production Queue -> QA -> Page Factory -> preview -> client validation -> technical QA -> explicit release -> verification -> DB feedback`

`SEO Production Queue` remains the canonical Page Queue.

Queue normalization is still needed infrastructure work, but it is not the client's next action and must not create bulk review work before the pilot proves the direction.

## New Practical Next Step

**External dependency:** Tasha sends the three-part source bundle for one wedding when ready.

**Execution after receipt:**

`source bundle -> canonical evidence/media/IDs -> queue -> complete pilot page -> finished preview -> Tasha validation`

If approved, convert the accepted pilot into the reusable content/page pattern and scale through the existing Page Factory.

## Core Lesson For This Project

Do not lead the client with architecture or volume. Demonstrate value with one finished, evidence-rich, voice-correct page and make the client's next action small and obvious.
