const state = {
  blocks: [],
  selectedBlock: null,
  selectedFile: null,
  executionId: null,
  result: null,
  detail: null,
  objectUrl: null,
};

const $ = (id) => document.getElementById(id);
const els = {
  healthBadge: $("healthBadge"), blockList: $("blockList"), blockCount: $("blockCount"),
  selectedBlockId: $("selectedBlockId"), selectedStatus: $("selectedStatus"), selectedTitle: $("selectedTitle"),
  selectedDescription: $("selectedDescription"), selectedVersion: $("selectedVersion"), selectedProvider: $("selectedProvider"),
  readinessValue: $("readinessValue"), readinessText: $("readinessText"), interactiveArea: $("interactiveArea"),
  comingSoon: $("comingSoon"), comingTitle: $("comingTitle"), comingText: $("comingText"), comingStatus: $("comingStatus"),
  dropZone: $("dropZone"), fileInput: $("fileInput"), fileSummary: $("fileSummary"), fileName: $("fileName"),
  fileSize: $("fileSize"), fileTypeIcon: $("fileTypeIcon"), previewWrap: $("previewWrap"), videoPreview: $("videoPreview"),
  audioPreview: $("audioPreview"), genericPreview: $("genericPreview"), runButton: $("runButton"), runButtonText: $("runButtonText"),
  spinner: $("spinner"), runHint: $("runHint"), clearButton: $("clearButton"), resultPanel: $("resultPanel"),
  resultSubtitle: $("resultSubtitle"), executionStatus: $("executionStatus"), warningList: $("warningList"),
  summaryCards: $("summaryCards"), rawJson: $("rawJson"), logList: $("logList"), toast: $("toast"),
};

function formatBytes(value) {
  if (value == null) return "—";
  const units = ["B", "KB", "MB", "GB", "TB"];
  let size = Number(value), index = 0;
  while (size >= 1024 && index < units.length - 1) { size /= 1024; index += 1; }
  return `${size >= 100 || index === 0 ? size.toFixed(0) : size.toFixed(1)} ${units[index]}`;
}

function formatDuration(value) {
  if (value == null || Number.isNaN(Number(value))) return "—";
  const total = Number(value);
  const hours = Math.floor(total / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const seconds = Math.floor(total % 60);
  const millis = Math.round((total - Math.floor(total)) * 1000);
  const body = `${String(minutes).padStart(2, "0")}:${String(seconds).padStart(2, "0")}`;
  return `${hours ? `${hours}:${body}` : body}${millis ? `.${String(millis).padStart(3, "0")}` : ""}`;
}

function showToast(message) {
  els.toast.textContent = message;
  els.toast.classList.remove("hidden");
  window.setTimeout(() => els.toast.classList.add("hidden"), 3200);
}

async function api(url, options = {}) {
  const response = await fetch(url, options);
  let payload = null;
  try { payload = await response.json(); } catch (_) { payload = null; }
  if (!response.ok) throw new Error(payload?.detail || `HTTP ${response.status}`);
  return payload;
}

function statusLabel(status) {
  return ({idea:"Idea", candidate:"Candidate", validated:"Validated", production:"Production"})[status] || status;
}

function renderBlocks() {
  els.blockCount.textContent = state.blocks.length;
  els.blockList.innerHTML = state.blocks.map(block => `
    <button class="block-card ${block.block_id === state.selectedBlock?.block_id ? "active" : ""}" data-block-id="${block.block_id}">
      <div class="block-card-top"><span class="block-id">${block.block_id}</span><span class="status-dot ${block.status}" title="${block.status}"></span></div>
      <p>${block.title}${block.interactive ? " · можно запустить" : ""}</p>
    </button>`).join("");
  document.querySelectorAll(".block-card").forEach(button => button.addEventListener("click", () => selectBlock(button.dataset.blockId)));
}

async function selectBlock(blockId) {
  const block = state.blocks.find(item => item.block_id === blockId);
  if (!block) return;
  state.selectedBlock = block;
  renderBlocks();
  els.selectedBlockId.textContent = block.block_id;
  els.selectedTitle.textContent = block.title;
  els.selectedDescription.textContent = block.description;
  els.selectedVersion.textContent = block.version;
  els.selectedProvider.textContent = block.provider;
  els.selectedStatus.textContent = block.status;
  els.selectedStatus.className = `status-badge ${block.status}`;
  els.readinessValue.textContent = statusLabel(block.status);
  els.readinessText.textContent = block.status === "idea"
    ? "Архитектура и назначение определены. Исполняемого кода пока нет."
    : block.status === "candidate"
      ? "Код и минимальные тесты есть. Реальная интеграция ещё проверяется."
      : "Блок прошёл реальную интеграцию.";

  if (block.interactive) {
    els.interactiveArea.classList.remove("hidden");
    els.comingSoon.classList.add("hidden");
    state.detail = await api(`/api/blocks/${encodeURIComponent(block.block_id)}`);
    renderStaticTabs();
  } else {
    els.interactiveArea.classList.add("hidden");
    els.comingSoon.classList.remove("hidden");
    els.comingTitle.textContent = `${block.title} пока не реализован`;
    els.comingText.textContent = `${block.description} Статус реестра: ${block.status}. ${block.limitations || ""}`;
    els.comingStatus.textContent = `${block.status} → candidate`;
  }
}

function renderStaticTabs() {
  if (!state.detail) return;
  const contract = state.detail.contract || {};
  $("tab-contract").innerHTML = `
    <div class="contract-grid">
      <div class="info-card"><h4>Операция</h4><p>${contract.operation || "—"}</p></div>
      <div class="info-card"><h4>Права</h4><ul>${(contract.permissions || []).map(x => `<li>${x}</li>`).join("")}</ul></div>
      <div class="info-card"><h4>BlockRequest</h4><ul>${(contract.request || []).map(x => `<li><code>${x}</code></li>`).join("")}</ul></div>
      <div class="info-card"><h4>BlockResult</h4><ul>${(contract.result || []).map(x => `<li><code>${x}</code></li>`).join("")}</ul></div>
    </div>`;
  const tests = state.detail.tests || {};
  $("tab-tests").innerHTML = `<div class="test-grid"><div class="info-card"><h4>Проверки готовности</h4>${Object.entries(tests).map(([key, value]) => {
    const success = value === "success" || String(value).includes("passed");
    return `<div class="test-line"><span>${key.replaceAll("_", " ")}</span><strong class="test-state ${success ? "success" : "pending"}">${value}</strong></div>`;
  }).join("")}</div><div class="info-card"><h4>Что означает Candidate</h4><p>Блок существует и проходит минимальные проверки. До Validated нужны Windows-проверка и подключение к реальному приложению.</p></div></div>`;
  const usage = state.detail.usage || {};
  $("tab-usage").innerHTML = `<div class="usage-grid"><div class="info-card"><h4>CLI</h4><pre class="code-block">${usage.cli || "—"}</pre></div><div class="info-card"><h4>Python</h4><pre class="code-block">${usage.python || "—"}</pre></div></div>`;
}

function previewFile(file) {
  if (state.objectUrl) URL.revokeObjectURL(state.objectUrl);
  state.objectUrl = URL.createObjectURL(file);
  els.videoPreview.classList.add("hidden");
  els.audioPreview.classList.add("hidden");
  els.genericPreview.classList.add("hidden");
  els.previewWrap.classList.remove("hidden");
  if (file.type.startsWith("video/")) {
    els.videoPreview.src = state.objectUrl;
    els.videoPreview.classList.remove("hidden");
  } else if (file.type.startsWith("audio/")) {
    els.audioPreview.src = state.objectUrl;
    els.audioPreview.classList.remove("hidden");
  } else {
    els.genericPreview.classList.remove("hidden");
  }
}

function selectFile(file) {
  state.selectedFile = file;
  els.fileSummary.classList.remove("hidden");
  els.fileName.textContent = file.name;
  els.fileSize.textContent = `${formatBytes(file.size)} · ${file.type || "неизвестный MIME"}`;
  els.fileTypeIcon.textContent = file.type.startsWith("audio/") ? "AUDIO" : file.type.startsWith("video/") ? "VIDEO" : "MEDIA";
  els.dropZone.classList.add("hidden");
  els.clearButton.classList.remove("hidden");
  els.runButton.disabled = false;
  els.runHint.textContent = "Файл будет обработан локально";
  els.resultPanel.classList.add("hidden");
  previewFile(file);
}

async function clearCurrent() {
  if (state.executionId) {
    try { await api(`/api/executions/${state.executionId}`, {method:"DELETE"}); } catch (_) {}
  }
  state.selectedFile = null;
  state.executionId = null;
  state.result = null;
  els.fileInput.value = "";
  els.fileSummary.classList.add("hidden");
  els.previewWrap.classList.add("hidden");
  els.dropZone.classList.remove("hidden");
  els.clearButton.classList.add("hidden");
  els.runButton.disabled = true;
  els.runHint.textContent = "Сначала выберите файл";
  els.resultPanel.classList.add("hidden");
  if (state.objectUrl) URL.revokeObjectURL(state.objectUrl);
  state.objectUrl = null;
}

function summaryCard(label, value) {
  return `<div class="summary-card"><span>${label}</span><strong>${value ?? "—"}</strong></div>`;
}

function renderExecution(payload) {
  state.executionId = payload.execution_id;
  state.result = payload;
  const result = payload.result;
  const success = result.status === "success";
  els.resultPanel.classList.remove("hidden");
  els.executionStatus.textContent = result.status.toUpperCase();
  els.executionStatus.className = `execution-status ${success ? "success" : "failed"}`;
  els.resultSubtitle.textContent = success ? `${payload.filename} успешно проанализирован.` : result.error?.message || "Выполнение завершилось ошибкой.";

  if (!success) {
    els.summaryCards.innerHTML = summaryCard("Код ошибки", result.error?.code || "unknown") + summaryCard("Можно повторить", result.error?.retryable ? "Да" : "Нет");
  } else {
    const artifact = result.output_artifacts[0] || {};
    const probe = artifact.metadata?.probe || {};
    const video = probe.primary_video || {};
    const audio = probe.primary_audio || {};
    els.summaryCards.innerHTML = [
      summaryCard("Длительность", formatDuration(probe.duration_seconds)),
      summaryCard("Разрешение", video.width && video.height ? `${video.width} × ${video.height}` : "—"),
      summaryCard("Формат", probe.format_name || "—"),
      summaryCard("Размер", formatBytes(probe.size_bytes)),
      summaryCard("Видеокодек", video.codec_name || "—"),
      summaryCard("FPS", video.frame_rate_fps ? Number(video.frame_rate_fps).toFixed(3).replace(/0+$/, "").replace(/\.$/, "") : "—"),
      summaryCard("Аудиокодек", audio.codec_name || "—"),
      summaryCard("Аудио", audio.sample_rate_hz ? `${Number(audio.sample_rate_hz).toLocaleString("ru-RU")} Hz · ${audio.channels || "?"} ch` : "—"),
    ].join("");
    renderOverview(probe, video, audio, result);
    renderStreams(probe.streams || []);
  }

  const warnings = result.warnings || [];
  els.warningList.classList.toggle("hidden", !warnings.length);
  els.warningList.innerHTML = warnings.map(item => `<div class="warning-item">${item}</div>`).join("");
  els.rawJson.textContent = JSON.stringify(payload, null, 2);
  els.logList.innerHTML = (payload.logs || []).map(entry => `<div class="log-entry"><span class="time">${entry.time.slice(11,23)}</span><span class="level ${entry.level}">${entry.level}</span><span>${entry.message}${Object.keys(entry.details || {}).length ? ` · ${JSON.stringify(entry.details)}` : ""}</span></div>`).join("");
  els.resultPanel.scrollIntoView({behavior:"smooth", block:"start"});
}

function renderOverview(probe, video, audio, result) {
  const rows = [
    ["Контейнер", probe.format_long_name || probe.format_name], ["Битрейт файла", probe.bit_rate ? `${Number(probe.bit_rate).toLocaleString("ru-RU")} bit/s` : "—"],
    ["Видео-потоков", probe.video_stream_count], ["Аудио-потоков", probe.audio_stream_count], ["Субтитров", probe.subtitle_stream_count],
    ["Pixel format", video.pixel_format || "—"], ["Channel layout", audio.channel_layout || "—"], ["Время выполнения", `${result.metrics?.elapsed_ms ?? "—"} ms`],
  ];
  $("tab-overview").innerHTML = `<div class="detail-grid">${rows.map(([label,value]) => `<div class="detail-row"><span>${label}</span><strong>${value ?? "—"}</strong></div>`).join("")}</div>`;
}

function renderStreams(streams) {
  if (!streams.length) { $("tab-streams").innerHTML = `<p>Потоки не обнаружены.</p>`; return; }
  $("tab-streams").innerHTML = `<div style="overflow:auto"><table class="stream-table"><thead><tr><th>#</th><th>Тип</th><th>Кодек</th><th>Размер / аудио</th><th>Длительность</th><th>Язык</th></tr></thead><tbody>${streams.map(s => `<tr><td>${s.index ?? "—"}</td><td>${s.codec_type || "—"}</td><td>${s.codec_name || "—"}</td><td>${s.width && s.height ? `${s.width}×${s.height}` : s.sample_rate_hz ? `${s.sample_rate_hz} Hz · ${s.channels || "?"} ch` : "—"}</td><td>${formatDuration(s.duration_seconds)}</td><td>${s.language || "—"}</td></tr>`).join("")}</tbody></table></div>`;
}

async function runProbe() {
  if (!state.selectedFile) return;
  els.runButton.disabled = true;
  els.spinner.classList.remove("hidden");
  els.runButtonText.textContent = "Анализирую файл…";
  els.runHint.textContent = "Выполняется локальный ffprobe";
  const form = new FormData();
  form.append("file", state.selectedFile);
  form.append("timeout_seconds", "60");
  try {
    const payload = await api("/api/blocks/media.probe/run", {method:"POST", body:form});
    renderExecution(payload);
    showToast("media.probe завершён");
  } catch (error) {
    showToast(error.message);
  } finally {
    els.runButton.disabled = false;
    els.spinner.classList.add("hidden");
    els.runButtonText.textContent = "Запустить media.probe";
    els.runHint.textContent = "Можно запустить повторно";
  }
}

function bindEvents() {
  document.querySelectorAll(".mode-button").forEach(button => button.addEventListener("click", () => {
    document.body.dataset.mode = button.dataset.mode;
    document.querySelectorAll(".mode-button").forEach(item => item.classList.toggle("active", item === button));
    if (button.dataset.mode === "owner" && document.querySelector(".tab.active")?.classList.contains("developer-only")) {
      document.querySelector('.tab[data-tab="overview"]').click();
    }
  }));
  els.fileInput.addEventListener("change", event => event.target.files?.[0] && selectFile(event.target.files[0]));
  ["dragenter","dragover"].forEach(name => els.dropZone.addEventListener(name, event => { event.preventDefault(); els.dropZone.classList.add("dragover"); }));
  ["dragleave","drop"].forEach(name => els.dropZone.addEventListener(name, event => { event.preventDefault(); els.dropZone.classList.remove("dragover"); }));
  els.dropZone.addEventListener("drop", event => event.dataTransfer.files?.[0] && selectFile(event.dataTransfer.files[0]));
  els.runButton.addEventListener("click", runProbe);
  els.clearButton.addEventListener("click", clearCurrent);
  document.querySelectorAll(".tab").forEach(tab => tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach(item => item.classList.toggle("active", item === tab));
    document.querySelectorAll(".tab-panel").forEach(panel => panel.classList.toggle("active", panel.id === `tab-${tab.dataset.tab}`));
  }));
}

async function initialize() {
  bindEvents();
  try {
    const [health, blocks] = await Promise.all([api("/api/health"), api("/api/blocks")]);
    els.healthBadge.className = `health-badge ${health.status}`;
    els.healthBadge.innerHTML = `<span></span> ${health.ffprobe.available ? "ffprobe готов · локальный режим" : "ffprobe не найден"}`;
    state.blocks = blocks;
    const initial = blocks.find(block => block.block_id === "media.probe") || blocks[0];
    await selectBlock(initial.block_id);
  } catch (error) {
    els.healthBadge.className = "health-badge degraded";
    els.healthBadge.innerHTML = "<span></span> Ошибка запуска";
    showToast(error.message);
  }
}

document.addEventListener("DOMContentLoaded", initialize);
