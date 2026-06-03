# YouTube transcript timing normalization prevents immediate scene playback stop

- Type: `verified-technical-solution`
- Lifecycle status: `active`
- Review status: `reviewed and accepted for selective reuse`
- Date: `2026-06-03`

## Problem

A YouTube scene player starts playback, runs briefly for about one second or less, and then freezes or stops.

The symptom may look like a YouTube IFrame API playback failure, autoplay issue, muted playback issue, or player recreation issue. In the verified case, the actual failure was incorrect transcript timestamp normalization.

## Investigation

The application loaded transcript entries through the `youtube-transcript` npm package and converted timestamps using unconditional division by `1000`:

```ts
start: entry.offset / 1000,
end: (entry.offset + entry.duration) / 1000,
```

The scene player also checked playback progress on an interval and stopped playback when:

```ts
currentTime >= sceneEndSeconds
```

The `youtube-transcript` package may expose transcript timing values in milliseconds or seconds depending on the transcript format or parser path. Unconditional division by `1000` can convert already-second-based values into fractions of a second.

Example:

```text
Expected scene end: 52 seconds
Incorrect normalized scene end: 0.052 seconds
```

The player then starts successfully and immediately stops itself because `currentTime >= sceneEndSeconds` becomes true almost at once.

## Verified Solution

Normalize transcript timing values before saving scene timestamps.

Use a millisecond-versus-seconds detection step:

```ts
function normalizeTranscriptTiming(offset: number, duration: number) {
  const shouldConvertFromMs = offset > 1000 || duration > 100
  const start = shouldConvertFromMs ? offset / 1000 : offset
  const normalizedDuration = shouldConvertFromMs ? duration / 1000 : duration

  return {
    start,
    end: start + normalizedDuration,
  }
}
```

Apply the same normalization in every transcript-loading path:

- direct browser transcript loading;
- development proxy or server-side transcript loading;
- any future backend transcript adapter.

Add a playback guard before auto-stop polling:

```ts
const sceneDuration = sceneEndSeconds - sceneStartSeconds

if (sceneEndSeconds <= sceneStartSeconds || sceneDuration < 1) {
  console.warn('Invalid scene timestamps; auto-stop disabled', {
    sceneStartSeconds,
    sceneEndSeconds,
    sceneDuration,
  })
  return
}
```

Keep diagnostic logs while validating:

```ts
console.log('Transcript timing diagnostic', {
  raw: transcript.slice(0, 3),
  normalized: normalizedTranscript.slice(0, 3),
})

console.log('YouTube scene playback diagnostic', {
  videoId,
  sceneStartSeconds,
  sceneEndSeconds,
  duration: sceneEndSeconds - sceneStartSeconds,
})
```

## Verification

Verified in project:

- Repository: `oleg3479881328-code/QuizLight`
- Player refactor commit: `212969bf7e7847eff52a45021a002c48ab83a1b2`
- Timing normalization commit: `1db03f12884e6737cd8e29e3b6bae8bcad152020`
- User confirmation after execution: playback works correctly.

## Important Reuse Note

Previously saved cards may still contain corrupted scene timestamps in browser `localStorage`.

After applying the fix, validate with a newly created card:

```text
reload page
-> load YouTube transcript again
-> select phrase again
-> save a new card
-> play the scene
```

Do not use an old saved card as the first validation case.

## Applies To

- web applications using `youtube-transcript`;
- YouTube IFrame API scene playback;
- timestamp-based clipping with `sceneStartSeconds` and `sceneEndSeconds`;
- browser or proxy transcript-loading pipelines.

## Triggers

Load this entry when:

- YouTube video starts and stops almost immediately;
- scene playback lasts about one second or less;
- `sceneEndSeconds` is unexpectedly below `1`;
- calculated scene duration is implausibly short;
- transcript timestamps are divided by `1000` without checking units;
- a player-side debugging effort does not explain an immediate stop.

## Do Not Load When

Do not treat this as the primary fix when:

- YouTube returns embed restriction errors `101` or `150`;
- YouTube returns missing referrer or client identification error `153`;
- the browser blocks autoplay;
- the video is unavailable;
- the transcript cannot be loaded at all;
- playback fails before any scene timestamp is applied.

## Risks And Limits

The threshold heuristic:

```ts
offset > 1000 || duration > 100
```

is practical but not mathematically universal. Very early transcript rows or unusual caption durations may be ambiguous.

For robust production code:

- inspect raw transcript values;
- log normalized values;
- centralize normalization in one reusable adapter;
- prefer explicit unit metadata or parser-specific normalization when available;
- add tests for seconds-based and milliseconds-based transcript samples.

## Related Standards

- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/REVIEW_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

## Reuse Rule

When a timestamp-clipped media player starts and immediately stops, inspect data normalization before redesigning the player architecture.
