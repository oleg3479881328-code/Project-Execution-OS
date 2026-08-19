export type EntityKind = string;

export interface StableEntityIdentity {
  id: string;
  kind: EntityKind;
  slug: string;
  parentId?: string | null;
}

export interface PublishedDocument<TContent = unknown> {
  entityId: string;
  kind: EntityKind;
  slug: string;
  publishId: string;
  publishedAt?: string | null;
  content: TContent;
}

export interface PublishedProjection<TProjection = unknown> {
  source: "published" | "fallback";
  entityId: string;
  projection: TProjection;
}

export type IndexingState = "preview_noindex" | "production_indexable";

export interface PublicationState {
  indexing: IndexingState;
  canonicalUrl: string;
  sitemapEligible: boolean;
}

export interface PublishRequest<TContent = unknown> {
  entity: StableEntityIdentity;
  content: TContent;
}

export interface PublishReceipt {
  publishId: string;
  durableSourceRef: string;
  deploymentRef?: string | null;
}

export interface PublicVersionVerification {
  publishId: string;
  publicUrl: string;
  visible: boolean;
  checkedAt: string;
}

export interface PublishAdapter<TContent = unknown> {
  publish(request: PublishRequest<TContent>): Promise<PublishReceipt>;
  verifyPublicVersion(receipt: PublishReceipt, publicUrl: string): Promise<PublicVersionVerification>;
}

export interface ResponsiveParityResult {
  viewport: { width: number; height: number };
  path: "published" | "fallback";
  horizontalOverflow: boolean;
  shellContractSatisfied: boolean;
  typographyFitsViewport: boolean;
}

export function assertStableEntityIdentity(entity: StableEntityIdentity): void {
  if (!entity.id || !entity.kind || !entity.slug) {
    throw new Error("Stable entity identity requires id, kind and slug");
  }
}

export function assertPublishedDocument<TContent>(doc: PublishedDocument<TContent>): void {
  if (!doc.entityId || !doc.kind || !doc.slug || !doc.publishId) {
    throw new Error("Published document envelope is incomplete");
  }
  if (doc.content === undefined || doc.content === null) {
    throw new Error("Published document content is required");
  }
}

export function resolvePublishedProjection<TContent, TProjection>(args: {
  entity: StableEntityIdentity;
  published: PublishedDocument<TContent> | null;
  fallback: TProjection;
  projectPublished: (doc: PublishedDocument<TContent>) => TProjection;
}): PublishedProjection<TProjection> {
  assertStableEntityIdentity(args.entity);

  if (args.published === null) {
    return {
      source: "fallback",
      entityId: args.entity.id,
      projection: args.fallback,
    };
  }

  assertPublishedDocument(args.published);
  if (args.published.entityId !== args.entity.id || args.published.kind !== args.entity.kind) {
    throw new Error("Published document identity does not match requested entity");
  }

  return {
    source: "published",
    entityId: args.entity.id,
    projection: args.projectPublished(args.published),
  };
}

export function assertPublicVersionVisible(verification: PublicVersionVerification, receipt: PublishReceipt): void {
  if (verification.publishId !== receipt.publishId) {
    throw new Error("Public version verification does not match publish receipt");
  }
  if (!verification.visible) {
    throw new Error("Published version is not yet visible at the public URL");
  }
}

export function assertResponsiveParity(results: ResponsiveParityResult[]): void {
  const published = results.filter((item) => item.path === "published");
  const fallback = results.filter((item) => item.path === "fallback");
  if (!published.length || !fallback.length) {
    throw new Error("Responsive parity requires both published and fallback evidence");
  }
  for (const item of results) {
    if (item.horizontalOverflow || !item.shellContractSatisfied || !item.typographyFitsViewport) {
      throw new Error(`Responsive parity failed for ${item.path} at ${item.viewport.width}x${item.viewport.height}`);
    }
  }
}
