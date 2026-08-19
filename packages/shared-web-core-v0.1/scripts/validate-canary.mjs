import fs from "node:fs";
import path from "node:path";
import process from "node:process";

const file = path.resolve("packages/shared-web-core-v0.1/canaries/tusia-runtime-canary.json");
const data = JSON.parse(fs.readFileSync(file, "utf8"));

const failures = [];
const requireValue = (condition, message) => {
  if (!condition) failures.push(message);
};

requireValue(data.evidenceType === "runtime-recovery", "canary must identify itself as runtime-recovery");
requireValue(data.sourceStatus === "original-source-not-located", "source status must stay explicit until original source is located");
requireValue(data.vercel?.deploymentState === "READY", "runtime canary must reference a READY deployment");
requireValue(data.runtime?.status === 200, "observed venue hub must have returned HTTP 200");
requireValue(data.runtime?.indexing === "preview_noindex", "preview canary must remain noindex");
requireValue(Array.isArray(data.runtime?.venuesObserved) && data.runtime.venuesObserved.length > 0, "runtime venue evidence is required");

const unknownInternals = [
  "stable-entity-identity",
  "published-cms-source-of-truth",
  "one-click-publish",
  "public-version-verification",
  "cms-fallback-responsive-parity",
];

for (const key of unknownInternals) {
  requireValue(data.capabilities?.[key] === "unknown", `${key} must remain unknown until direct source/runtime evidence exists`);
}

if (failures.length) {
  console.error("TUSIA CANARY FAIL");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log("TUSIA CANARY PASS");
console.log(`deployment=${data.vercel.deploymentId}`);
console.log(`venuesObserved=${data.runtime.venuesObserved.length}`);
