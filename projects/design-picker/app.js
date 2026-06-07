const STORAGE_KEY = "design-picker-catalog-v3";
const STATUS_ORDER = { primary: 0, partial: 1, undecided: 2, rejected: 3 };
const PATTERN_OPTIONS = [
  "hero",
  "cards",
  "pricing",
  "navigation",
  "motion",
  "dashboard",
  "onboarding",
  "checkout",
  "custom"
];

const STATUS_LABELS = {
  primary: "Primary",
  partial: "Partial",
  rejected: "Rejected",
  undecided: "Undecided"
};

const seedDonors = [
  {
    id: crypto.randomUUID(),
    title: "Linear",
    sourceUrl: "https://linear.app",
    manualPreviewUrl: "",
    projectType: "SaaS product",
    styleTags: ["minimal", "dark", "premium"],
    sectionTags: ["hero", "navigation", "product"],
    decision: "partial",
    patterns: ["hero", "navigation", "motion"],
    notes: "Use the calm density and product-led framing. Do not copy the exact dark palette.",
    strongPoints: "Strong visual hierarchy and mature interface tone.",
    previewMeta: {
      provider: "screenshot_api",
      status: "ready",
      capturedAt: new Date().toISOString(),
      viewport: "desktop",
      refreshNonce: 0
    },
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString()
  },
  {
    id: crypto.randomUUID(),
    title: "Stripe",
    sourceUrl: "https://stripe.com",
    manualPreviewUrl: "",
    projectType: "Marketing site",
    styleTags: ["technical", "light", "clear"],
    sectionTags: ["hero", "pricing", "trust"],
    decision: "undecided",
    patterns: ["hero", "pricing"],
    notes: "Good reference for explanation sequence and proof blocks.",
    strongPoints: "Clear product storytelling with strong section pacing.",
    previewMeta: {
      provider: "screenshot_api",
      status: "ready",
      capturedAt: new Date().toISOString(),
      viewport: "desktop",
      refreshNonce: 0
    },
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString()
  }
];

const previewAdapter = {
  providers: {
    manual(donor) {
      if (!donor.manualPreviewUrl?.trim()) {
        return null;
      }

      return {
        imageUrl: normalizeUrl(donor.manualPreviewUrl),
        provider: "manual",
        status: "ready",
        capturedAt: donor.previewMeta?.capturedAt || donor.updatedAt || new Date().toISOString(),
        fallbackLabel: "Manual preview"
      };
    },

    screenshotApi(donor) {
      const normalized = normalizeUrl(donor.sourceUrl);

      if (!normalized) {
        return null;
      }

      const cacheBuster = donor.previewMeta?.refreshNonce || 0;
      return {
        imageUrl: `https://image.thum.io/get/width/1440/crop/900/noanimate/${normalized}?refresh=${cacheBuster}`,
        provider: "screenshot_api",
        status: "ready",
        capturedAt: donor.previewMeta?.capturedAt || donor.updatedAt || new Date().toISOString(),
        fallbackLabel: "Auto preview"
      };
    }
  },

  capture(donor) {
    return this.providers.manual(donor) || this.providers.screenshotApi(donor) || {
      imageUrl: "",
      provider: "placeholder",
      status: "failed",
      capturedAt: donor.previewMeta?.capturedAt || donor.updatedAt || new Date().toISOString(),
      fallbackLabel: "Preview unavailable"
    };
  }
};

const state = {
  donors: loadDonors(),
  editingId: null
};

const nodes = {
  heroStats: document.getElementById("heroStats"),
  boardSummary: document.getElementById("boardSummary"),
  cardGrid: document.getElementById("cardGrid"),
  searchInput: document.getElementById("searchInput"),
  statusFilter: document.getElementById("statusFilter"),
  patternFilter: document.getElementById("patternFilter"),
  sortMode: document.getElementById("sortMode"),
  openCreateButton: document.getElementById("openCreateButton"),
  exportMarkdownButton: document.getElementById("exportMarkdownButton"),
  exportJsonButton: document.getElementById("exportJsonButton"),
  editorDialog: document.getElementById("editorDialog"),
  editorForm: document.getElementById("editorForm"),
  closeDialogButton: document.getElementById("closeDialogButton"),
  cancelButton: document.getElementById("cancelButton"),
  dialogTitle: document.getElementById("dialogTitle"),
  sourceUrlInput: document.getElementById("sourceUrlInput"),
  titleInput: document.getElementById("titleInput"),
  projectTypeInput: document.getElementById("projectTypeInput"),
  manualPreviewInput: document.getElementById("manualPreviewInput"),
  styleTagsInput: document.getElementById("styleTagsInput"),
  sectionTagsInput: document.getElementById("sectionTagsInput"),
  decisionInput: document.getElementById("decisionInput"),
  strongPointsInput: document.getElementById("strongPointsInput"),
  notesInput: document.getElementById("notesInput"),
  patternChecklist: document.getElementById("patternChecklist"),
  emptyStateTemplate: document.getElementById("emptyStateTemplate")
};

hydratePatternOptions();
bindEvents();
render();

function loadDonors() {
  const raw = localStorage.getItem(STORAGE_KEY);

  if (!raw) {
    return structuredClone(seedDonors);
  }

  try {
    const parsed = JSON.parse(raw);
    return Array.isArray(parsed) && parsed.length ? parsed : structuredClone(seedDonors);
  } catch {
    return structuredClone(seedDonors);
  }
}

function persist() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.donors));
}

function bindEvents() {
  nodes.openCreateButton.addEventListener("click", () => openEditor());
  nodes.closeDialogButton.addEventListener("click", closeEditor);
  nodes.cancelButton.addEventListener("click", closeEditor);
  nodes.searchInput.addEventListener("input", render);
  nodes.statusFilter.addEventListener("change", render);
  nodes.patternFilter.addEventListener("change", render);
  nodes.sortMode.addEventListener("change", render);
  nodes.exportMarkdownButton.addEventListener("click", exportMarkdown);
  nodes.exportJsonButton.addEventListener("click", exportJson);
  nodes.editorForm.addEventListener("submit", saveEditor);
  nodes.editorDialog.addEventListener("cancel", event => {
    event.preventDefault();
    closeEditor();
  });
}

function hydratePatternOptions() {
  nodes.patternFilter.insertAdjacentHTML(
    "beforeend",
    PATTERN_OPTIONS.map(pattern => `<option value="${pattern}">${pattern}</option>`).join("")
  );

  nodes.patternChecklist.innerHTML = PATTERN_OPTIONS.map(pattern => `
    <label class="pattern-toggle">
      <input type="checkbox" value="${pattern}" />
      <span>${pattern}</span>
    </label>
  `).join("");
}

function render() {
  const donors = getFilteredDonors();
  renderHeroStats();
  renderBoardSummary();
  renderCardGrid(donors);
}

function renderHeroStats() {
  const primary = state.donors.filter(donor => donor.decision === "primary").length;
  const partial = state.donors.filter(donor => donor.decision === "partial").length;
  const withManualPreview = state.donors.filter(donor => donor.manualPreviewUrl?.trim()).length;
  const patterns = new Set(state.donors.flatMap(donor => donor.patterns || []));

  nodes.heroStats.innerHTML = [
    { value: state.donors.length, label: "saved donors" },
    { value: primary, label: "primary picks" },
    { value: partial, label: "partial references" },
    { value: patterns.size, label: "pattern types selected" },
    { value: withManualPreview, label: "manual preview overrides" }
  ].map(stat => `
    <article class="hero-stat">
      <strong>${stat.value}</strong>
      <span>${stat.label}</span>
    </article>
  `).join("");
}

function renderBoardSummary() {
  const countsByStatus = Object.keys(STATUS_LABELS).map(status => ({
    status,
    count: state.donors.filter(donor => donor.decision === status).length
  }));

  const topPatterns = PATTERN_OPTIONS
    .map(pattern => ({
      pattern,
      count: state.donors.filter(donor => (donor.patterns || []).includes(pattern)).length
    }))
    .filter(entry => entry.count > 0)
    .sort((left, right) => right.count - left.count)
    .slice(0, 4);

  nodes.boardSummary.innerHTML = `
    <div>
      <p class="section-kicker">Selection board</p>
      <h3>See the shortlist shape before exporting.</h3>
      <p class="hero-text">This board stays local in the browser, survives reloads, and keeps the preview provider behind one adapter seam for later Linkwarden integration.</p>
    </div>
    <div class="board-summary-grid">
      ${countsByStatus.map(item => `
        <article class="summary-card">
          <strong class="status-${item.status}">${item.count}</strong>
          <span>${STATUS_LABELS[item.status]} donors</span>
        </article>
      `).join("")}
      <article class="summary-card">
        <strong>${topPatterns.length}</strong>
        <span>top active patterns</span>
        <ul>
          ${topPatterns.length ? topPatterns.map(item => `<li>${item.pattern}: ${item.count}</li>`).join("") : "<li>No patterns selected yet.</li>"}
        </ul>
      </article>
    </div>
  `;
}

function renderCardGrid(donors) {
  if (!donors.length) {
    nodes.cardGrid.replaceChildren(nodes.emptyStateTemplate.content.cloneNode(true));
    return;
  }

  nodes.cardGrid.innerHTML = donors.map(donor => {
    const preview = previewAdapter.capture(donor);
    const providerLabel = preview.provider === "manual"
      ? "Manual preview"
      : preview.provider === "screenshot_api"
        ? "Auto screenshot"
        : "Fallback";

    return `
      <article class="donor-card">
        <div class="donor-preview">
          ${preview.imageUrl
            ? `<img src="${escapeHtml(preview.imageUrl)}" alt="${escapeHtml(donor.title)} preview" data-fallback-title="${escapeHtml(donor.title)}" data-fallback-domain="${escapeHtml(getDomainLabel(donor.sourceUrl))}" onerror="window.__designPickerHandlePreviewError(event)" />`
            : ""}
          ${!preview.imageUrl ? buildFallbackMarkup(donor, preview.fallbackLabel) : ""}
          <div class="preview-chip-row">
            <span class="chip">${providerLabel}</span>
            <span class="chip">${formatDate(preview.capturedAt)}</span>
          </div>
        </div>
        <div class="donor-body">
          <div class="donor-header">
            <div>
              <p class="section-kicker">Donor</p>
              <h3 class="donor-title">${escapeHtml(donor.title)}</h3>
            </div>
            <span class="meta-pill status-chip status-${donor.decision}">${STATUS_LABELS[donor.decision]}</span>
          </div>

          <a class="donor-url" href="${escapeHtml(donor.sourceUrl)}" target="_blank" rel="noreferrer">${escapeHtml(donor.sourceUrl)}</a>

          <div class="meta-cluster">
            <span class="meta-pill">${escapeHtml(donor.projectType || "Project type not set")}</span>
            <span class="meta-pill">${escapeHtml(getDomainLabel(donor.sourceUrl))}</span>
            <span class="meta-pill">${preview.provider === "manual" ? "Manual override active" : "Adapter preview"}</span>
          </div>

          ${renderPillCluster("Style tags", donor.styleTags, "tag")}
          ${renderPillCluster("Section tags", donor.sectionTags, "tag")}
          ${renderPillCluster("Patterns", donor.patterns, "pattern")}

          <div>
            <p class="subheading">Strong points</p>
            <div class="donor-copy">${escapeHtml(donor.strongPoints || "Not captured yet.")}</div>
          </div>

          <div>
            <p class="subheading">Notes</p>
            <div class="donor-copy">${escapeHtml(donor.notes || "No notes yet.")}</div>
          </div>

          <div class="action-row">
            <button class="button button-primary" type="button" data-action="edit" data-id="${donor.id}">Edit</button>
            <button class="button button-secondary" type="button" data-action="refresh" data-id="${donor.id}">Refresh preview</button>
            <button class="button button-ghost" type="button" data-action="delete" data-id="${donor.id}">Delete</button>
          </div>
        </div>
      </article>
    `;
  }).join("");

  nodes.cardGrid.querySelectorAll("[data-action]").forEach(button => {
    button.addEventListener("click", () => handleCardAction(button.dataset.action, button.dataset.id));
  });
}

function renderPillCluster(label, values, kind) {
  if (!values?.length) {
    return "";
  }

  const className = kind === "pattern" ? "pattern-pill" : "tag-pill";
  return `
    <div>
      <p class="subheading">${label}</p>
      <div class="${kind}-cluster">
        ${values.map(value => `<span class="${className}">${escapeHtml(value)}</span>`).join("")}
      </div>
    </div>
  `;
}

function buildFallbackMarkup(donor, label) {
  return `
    <div class="preview-overlay">
      <div>
        <strong>${escapeHtml(donor.title)}</strong>
        <div>${escapeHtml(getDomainLabel(donor.sourceUrl))}</div>
        <div>${escapeHtml(label)}</div>
      </div>
    </div>
  `;
}

function handleCardAction(action, id) {
  if (action === "edit") {
    const donor = state.donors.find(item => item.id === id);
    if (donor) {
      openEditor(donor);
    }
    return;
  }

  if (action === "refresh") {
    state.donors = state.donors.map(donor => donor.id === id ? {
      ...donor,
      previewMeta: {
        ...(donor.previewMeta || {}),
        provider: donor.manualPreviewUrl?.trim() ? "manual" : "screenshot_api",
        status: donor.manualPreviewUrl?.trim() ? "ready" : "pending",
        capturedAt: new Date().toISOString(),
        refreshNonce: Date.now()
      },
      updatedAt: new Date().toISOString()
    } : donor);
    persist();
    render();
    return;
  }

  if (action === "delete") {
    state.donors = state.donors.filter(donor => donor.id !== id);
    persist();
    render();
  }
}

function openEditor(donor = null) {
  state.editingId = donor?.id || null;
  nodes.dialogTitle.textContent = donor ? "Edit donor" : "Add donor";
  nodes.sourceUrlInput.value = donor?.sourceUrl || "";
  nodes.titleInput.value = donor?.title || "";
  nodes.projectTypeInput.value = donor?.projectType || "";
  nodes.manualPreviewInput.value = donor?.manualPreviewUrl || "";
  nodes.styleTagsInput.value = (donor?.styleTags || []).join(", ");
  nodes.sectionTagsInput.value = (donor?.sectionTags || []).join(", ");
  nodes.decisionInput.value = donor?.decision || "undecided";
  nodes.strongPointsInput.value = donor?.strongPoints || "";
  nodes.notesInput.value = donor?.notes || "";

  nodes.patternChecklist.querySelectorAll("input").forEach(input => {
    input.checked = donor?.patterns?.includes(input.value) || false;
  });

  nodes.editorDialog.showModal();
}

function closeEditor() {
  nodes.editorDialog.close();
  state.editingId = null;
  nodes.editorForm.reset();
  nodes.patternChecklist.querySelectorAll("input").forEach(input => {
    input.checked = false;
  });
}

function saveEditor(event) {
  event.preventDefault();

  const sourceUrl = normalizeUrl(nodes.sourceUrlInput.value);
  if (!sourceUrl) {
    nodes.sourceUrlInput.focus();
    return;
  }

  const existing = state.editingId ? state.donors.find(donor => donor.id === state.editingId) : null;
  const now = new Date().toISOString();
  const manualPreviewUrl = normalizeUrl(nodes.manualPreviewInput.value, { allowImageOnly: true });

  const donor = {
    id: state.editingId || crypto.randomUUID(),
    title: nodes.titleInput.value.trim() || titleFromUrl(sourceUrl),
    sourceUrl,
    manualPreviewUrl,
    projectType: nodes.projectTypeInput.value.trim(),
    styleTags: parseTagInput(nodes.styleTagsInput.value),
    sectionTags: parseTagInput(nodes.sectionTagsInput.value),
    decision: nodes.decisionInput.value,
    patterns: getPatternSelection(),
    notes: nodes.notesInput.value.trim(),
    strongPoints: nodes.strongPointsInput.value.trim(),
    previewMeta: {
      provider: manualPreviewUrl ? "manual" : "screenshot_api",
      status: "ready",
      capturedAt: now,
      viewport: "desktop",
      refreshNonce: existing?.previewMeta?.refreshNonce || 0
    },
    createdAt: existing?.createdAt || now,
    updatedAt: now
  };

  const duplicate = state.donors.find(item => item.id !== donor.id && normalizeUrl(item.sourceUrl) === donor.sourceUrl);
  if (duplicate) {
    const shouldReplace = window.confirm(`A donor for ${donor.sourceUrl} already exists. Replace the existing record?`);
    if (!shouldReplace) {
      return;
    }

    state.donors = state.donors.filter(item => item.id !== duplicate.id);
  }

  state.donors = state.editingId
    ? state.donors.map(item => item.id === state.editingId ? donor : item)
    : [donor, ...state.donors];

  persist();
  closeEditor();
  render();
}

function getFilteredDonors() {
  const query = nodes.searchInput.value.trim().toLowerCase();
  const status = nodes.statusFilter.value;
  const pattern = nodes.patternFilter.value;
  const sortMode = nodes.sortMode.value;

  const filtered = state.donors.filter(donor => {
    const haystack = [
      donor.title,
      donor.sourceUrl,
      donor.projectType,
      donor.notes,
      donor.strongPoints,
      ...(donor.styleTags || []),
      ...(donor.sectionTags || []),
      ...(donor.patterns || [])
    ].join(" ").toLowerCase();

    const matchesQuery = !query || haystack.includes(query);
    const matchesStatus = status === "all" || donor.decision === status;
    const matchesPattern = pattern === "all" || (donor.patterns || []).includes(pattern);
    return matchesQuery && matchesStatus && matchesPattern;
  });

  return filtered.sort((left, right) => {
    if (sortMode === "title") {
      return left.title.localeCompare(right.title);
    }

    if (sortMode === "status") {
      return (STATUS_ORDER[left.decision] ?? 99) - (STATUS_ORDER[right.decision] ?? 99) ||
        right.updatedAt.localeCompare(left.updatedAt);
    }

    return right.updatedAt.localeCompare(left.updatedAt);
  });
}

function exportMarkdown() {
  const grouped = groupByStatus(state.donors);
  const markdown = `# Design Selection Record

Generated: ${new Date().toISOString()}

## Primary Direction
${renderMarkdownList(grouped.primary)}

## Partial References
${renderMarkdownList(grouped.partial)}

## Rejected Directions
${renderMarkdownList(grouped.rejected)}

## Undecided Donors
${renderMarkdownList(grouped.undecided)}
`;

  downloadFile("design-selection-record.md", markdown, "text/markdown");
}

function exportJson() {
  const enriched = state.donors.map(donor => ({
    ...donor,
    preview: previewAdapter.capture(donor)
  }));
  downloadFile("design-picker-donors.json", JSON.stringify(enriched, null, 2), "application/json");
}

function groupByStatus(donors) {
  return donors.reduce((groups, donor) => {
    groups[donor.decision].push(donor);
    return groups;
  }, {
    primary: [],
    partial: [],
    rejected: [],
    undecided: []
  });
}

function renderMarkdownList(donors) {
  if (!donors.length) {
    return "- None.\n";
  }

  return donors.map(donor => {
    const preview = previewAdapter.capture(donor);
    return `### ${donor.title}
- URL: ${donor.sourceUrl}
- Decision: ${STATUS_LABELS[donor.decision]}
- Project type: ${donor.projectType || "Not set"}
- Patterns: ${(donor.patterns || []).join(", ") || "None"}
- Style tags: ${(donor.styleTags || []).join(", ") || "None"}
- Section tags: ${(donor.sectionTags || []).join(", ") || "None"}
- Strong points: ${donor.strongPoints || "Not captured"}
- Notes: ${donor.notes || "No notes"}
- Preview source: ${preview.provider}
- Preview URL: ${preview.imageUrl || "Fallback only"}
`;
  }).join("\n");
}

function downloadFile(filename, content, contentType) {
  const blob = new Blob([content], { type: contentType });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

function parseTagInput(value) {
  return value
    .split(",")
    .map(item => item.trim())
    .filter(Boolean);
}

function getPatternSelection() {
  return [...nodes.patternChecklist.querySelectorAll("input:checked")].map(input => input.value);
}

function titleFromUrl(sourceUrl) {
  return getDomainLabel(sourceUrl);
}

function getDomainLabel(value) {
  try {
    return new URL(normalizeUrl(value)).hostname.replace(/^www\./, "");
  } catch {
    return value.trim();
  }
}

function normalizeUrl(value, options = {}) {
  const trimmed = value.trim();
  if (!trimmed) {
    return "";
  }

  if (options.allowImageOnly && /^(data:image\/|blob:)/i.test(trimmed)) {
    return trimmed;
  }

  return /^https?:\/\//i.test(trimmed) ? trimmed : `https://${trimmed}`;
}

function formatDate(value) {
  if (!value) {
    return "Fresh";
  }

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) {
    return "Fresh";
  }

  return date.toLocaleDateString(undefined, {
    month: "short",
    day: "numeric"
  });
}

function escapeHtml(value = "") {
  return String(value).replace(/[&<>"']/g, character => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;"
  })[character]);
}

window.__designPickerHandlePreviewError = function handlePreviewError(event) {
  const image = event.target;
  const title = image.dataset.fallbackTitle || "Preview unavailable";
  const domain = image.dataset.fallbackDomain || "";
  image.replaceWith(createFallbackNode(title, domain));
};

function createFallbackNode(title, domain) {
  const wrapper = document.createElement("div");
  wrapper.className = "preview-overlay";
  wrapper.innerHTML = `
    <div>
      <strong>${escapeHtml(title)}</strong>
      <div>${escapeHtml(domain)}</div>
      <div>Preview unavailable. Use manual override if needed.</div>
    </div>
  `;
  return wrapper;
}
