# Showit Whole New Page From Any Point — PROVEN LIVE

Date: 2026-09-30
Status: `LIVE-PROVEN / CURRENT ACCEPTED PROOF`

## Goal

Prove that the Showit adapter can start from any location inside an already-open authenticated Showit design and create a completely new page without using an existing page or Canvas as a donor.

## Proven execution path

```text
any point inside authenticated Showit design
→ discover current site/design
→ load current site model + ETag
→ generate fresh page ID
→ build new page JSON entirely in memory
→ build 4 new Canvas blocks + 17 text elements entirely in memory
→ save brand-new page file with isNew:true
→ durable S3 page-file readback
→ refresh site model + current root ETag
→ register the new page in site items/pages
→ save site manifest
→ durable site-manifest readback
→ update Showit init_page_id
→ reload editor
→ open/read the new page
→ verify new page resource was loaded
```

## Accepted live result

```text
status: WHOLE_NEW_PAGE_CREATED_AND_LINKED
siteDesignId: 732235
designKey: ljhcybjw0lbnr_qqyok5ma
pageId: WF1CV1p74
pageName: API FULL PAGE — FROM SCRATCH-1
pageSlug: api-full-page-from-scratch-1
pageETag: 28d4d731c2953c4a05a5f3bca541ba33
rootOldETag: 65ec5a19425ce327c13189b47cae2af4
rootNewETag: 88489abb63637eccc500e4ecf52b1014
pageReadback.attempt: 1
pageReadback.blocks: 4
pageReadback.elements: 17
manifestReadback.attempt: 1
manifestReadback.pageIndex: 26
manifestReadback.totalPages: 27
blocks: 4
elements: 17
initPageUpdated: true
creationMode: NEW PAGE + NEW CANVAS + NEW ELEMENTS — NO SOURCE PAGE USED
editorReloaded: true
newPageLoaded: true
pageNameCount: 1
newPageResourceSeen: true
finalStatus: SHOWIT WHOLE NEW PAGE FROM ANY POINT — PROOF COMPLETED
```

The `-1` suffix is expected because a page using the base test name/slug already existed; the builder selected a unique name/slug instead of colliding.

## What is now proven

- The adapter does not need the currently selected Canvas or page as a donor.
- A completely new Showit page file can be generated from JSON in memory.
- Multiple new Canvas blocks and multiple new elements can be committed in one page-file save.
- The new page can be registered in the Showit site model in a separate manifest save.
- Both page-file and site-manifest writes can be verified by durable readback before trusting editor UI state.
- The new page can be opened after reload and its page resource is actually fetched.
- Start position inside the editor is no longer a dependency for this route; the dependency is only that the correct target Showit design is open and authenticated.

## Architecture consequence

For supported static page content, the accepted Showit creation route is now:

```text
Universal Recipe / generated page intent
→ Showit page JSON compiler
→ brand-new page file
→ one page-file save for all Canvas/elements
→ register page in site model
→ manifest save
→ durable readback
→ editor reload / visual QA
```

This supersedes the earlier assumption that building a new Showit page would require UI creation or element-by-element editor operations.

## Boundaries not yet proven

Do not overstate this milestone. The live proof used static text elements and Canvas backgrounds. It does not yet prove:

- media upload/import and Showit media-library binding;
- image elements using newly uploaded assets;
- galleries, video, Lottie or embeds;
- arbitrary interaction/link/state/motion translation;
- exact full Universal Page Recipe → Showit reconstruction of a real donor page;
- publish/production acceptance for a generated page.

## Next acceptance gate

The highest-value next proof is the media boundary:

```text
start from any point
→ create another brand-new page
→ upload/import one image through the real Showit media path
→ bind that asset to a new image element in page JSON
→ one page-file save
→ durable readback
→ reload
→ visual verification that the image renders
```

Once media is live-proven, proceed to a real captured Universal Page Recipe → Showit page compile rather than adding more synthetic text-only tests.

## Security rule

Never persist or print the real Showit auth token. Runtime may read `localStorage.authToken` only inside the already-authenticated user session and use it for Showit's own internal API calls.
