import {
  assertPublicVersionVisible,
  assertResponsiveParity,
  resolvePublishedProjection,
  type PublishedDocument,
  type StableEntityIdentity,
} from "../src/contracts";

type OlgaBlock = {
  type: string;
  props?: Record<string, unknown>;
};

type OlgaTemplateData = {
  root?: { props?: Record<string, unknown> };
  content: OlgaBlock[];
  zones?: Record<string, unknown>;
};

const entity: StableEntityIdentity = {
  id: "ven_001",
  kind: "venue",
  slug: "peterloon-estate",
};

// Mirrors the current Olga production storage shape: stable entity ID is held
// in the entity registry, while the published JSON stores kind + slug + data
// and currently does not require entityId or publishId in the document itself.
const published: PublishedDocument<OlgaTemplateData> = {
  kind: "venue",
  slug: "peterloon-estate",
  content: {
    root: { props: {} },
    content: [
      {
        type: "VenueHero",
        props: {
          title: "Peterloon Estate",
          imageUrl: "/editor-assets/templates/venue/peterloon-estate/example.jpg",
        },
      },
    ],
    zones: {},
  },
};

const resolved = resolvePublishedProjection({
  entity,
  published,
  fallback: { title: "STATIC" },
  projectPublished: (doc) => {
    const hero = doc.content.content.find((block) => block.type === "VenueHero");
    return { title: String(hero?.props?.title ?? "") };
  },
});

if (resolved.source !== "published" || resolved.entityId !== "ven_001" || resolved.projection.title !== "Peterloon Estate") {
  throw new Error("Olga published-content canary failed");
}

const fallback = resolvePublishedProjection({
  entity,
  published: null,
  fallback: { title: "STATIC" },
  projectPublished: () => ({ title: "SHOULD_NOT_RUN" }),
});

if (fallback.source !== "fallback" || fallback.projection.title !== "STATIC") {
  throw new Error("Olga fallback canary failed");
}

let mismatchRejected = false;
try {
  resolvePublishedProjection({
    entity,
    published: { ...published, slug: "wrong-slug" },
    fallback: { title: "STATIC" },
    projectPublished: () => ({ title: "INVALID" }),
  });
} catch {
  mismatchRejected = true;
}
if (!mismatchRejected) throw new Error("Published slug mismatch must fail loudly");

assertPublicVersionVisible(
  {
    publishId: "pub_123",
    publicUrl: "https://venues.olgapoloweddings.com/peterloon-estate",
    visible: true,
    checkedAt: "2026-08-19T19:20:00Z",
  },
  {
    publishId: "pub_123",
    durableSourceRef: "github:olga-polo-weddings-web/main",
  },
);

assertResponsiveParity([
  {
    viewport: { width: 390, height: 844 },
    path: "published",
    horizontalOverflow: false,
    shellContractSatisfied: true,
    typographyFitsViewport: true,
  },
  {
    viewport: { width: 390, height: 844 },
    path: "fallback",
    horizontalOverflow: false,
    shellContractSatisfied: true,
    typographyFitsViewport: true,
  },
]);

console.log("OLGA_SHARED_CORE_CANARY_PASS");
