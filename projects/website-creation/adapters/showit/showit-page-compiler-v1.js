(() => {
  "use strict";

  const VERSION = "1.0.0-candidate";
  const GLOBAL_NAME = "ShowitPageCompilerV1";
  const API_BASE = "https://api.showit.com";
  const PAGE_RESOURCE_RE = /designs\.showit\.co\/([^/]+)\/pages\/([^/?]+)\.json/i;
  const ID_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-";

  const fail = (code, details = {}) => {
    const error = new Error(`${code} ${JSON.stringify(details)}`);
    error.code = code;
    error.details = details;
    throw error;
  };

  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

  const clone = value => {
    if (typeof structuredClone === "function") return structuredClone(value);
    return JSON.parse(JSON.stringify(value));
  };

  const stable = value => {
    if (Array.isArray(value)) return value.map(stable);
    if (value && typeof value === "object") {
      return Object.keys(value)
        .sort()
        .reduce((out, key) => {
          out[key] = stable(value[key]);
          return out;
        }, {});
    }
    return value;
  };

  const stableStringify = value => JSON.stringify(stable(value));

  const stripEtag = value =>
    String(value || "")
      .replace(/^W\//, "")
      .replace(/^"+|"+$/g, "");

  const assertEnvironment = () => {
    if (location.hostname !== "app.showit.com") {
      fail("NOT_SHOWIT_APP", { href: location.href });
    }
  };

  const getAuthToken = () => {
    assertEnvironment();
    const token = localStorage.getItem("authToken");
    if (!token) fail("SHOWIT_AUTH_TOKEN_NOT_FOUND");
    return token;
  };

  const authHeaders = extra => ({
    Accept: "*/*",
    Authorization: `Bearer ${getAuthToken()}`,
    ...(extra || {})
  });

  const makeId = existingBlockData => {
    const existing = existingBlockData || {};
    let id;
    do {
      const bytes = new Uint8Array(9);
      crypto.getRandomValues(bytes);
      id = Array.from(bytes, b => ID_ALPHABET[b % ID_ALPHABET.length]).join("");
    } while (existing[id]);
    return id;
  };

  const discoverCurrentPage = () => {
    assertEnvironment();

    const resources = performance
      .getEntriesByType("resource")
      .map(entry => entry.name)
      .filter(Boolean)
      .filter(url => PAGE_RESOURCE_RE.test(url));

    if (!resources.length) {
      fail("CURRENT_PAGE_RESOURCE_NOT_FOUND", {
        hint: "Reload Showit, wait for the editor to finish loading, then install/run the compiler again."
      });
    }

    const currentResource = resources[resources.length - 1];
    const match = currentResource.match(PAGE_RESOURCE_RE);

    if (!match) fail("PAGE_RESOURCE_PARSE_FAILED", { currentResource });

    const designKey = decodeURIComponent(match[1]);
    const pageId = decodeURIComponent(match[2]);

    return { currentResource, designKey, pageId };
  };

  const makePageUrl = ({ designKey, pageId }) =>
    `https://s3-external-1.amazonaws.com/designs.showit.co/${encodeURIComponent(
      designKey
    )}/pages/${encodeURIComponent(pageId)}.json?t=${Date.now()}&probe=${Math.random()}`;

  const loadPage = async () => {
    const page = discoverCurrentPage();
    const response = await fetch(makePageUrl(page), {
      method: "GET",
      cache: "no-store"
    });

    if (!response.ok) {
      fail("PAGE_LOAD_FAILED", {
        status: response.status,
        statusText: response.statusText,
        page
      });
    }

    const eTag = stripEtag(response.headers.get("etag"));
    const data = await response.json();

    if (!eTag) fail("ETAG_MISSING", { page });
    if (!data || !Array.isArray(data.blocks) || !data.blockData) {
      fail("UNEXPECTED_PAGE_MODEL", { page });
    }

    return { ...page, eTag, data };
  };

  const gzipJson = async value => {
    if (typeof CompressionStream !== "function") {
      fail("COMPRESSIONSTREAM_UNAVAILABLE");
    }

    const rawJson = JSON.stringify(value);
    const stream = new Blob([rawJson], { type: "application/json" })
      .stream()
      .pipeThrough(new CompressionStream("gzip"));
    const bytes = await new Response(stream).arrayBuffer();

    return {
      rawJson,
      rawJsonBytes: new TextEncoder().encode(rawJson).length,
      gzipBytes: bytes.byteLength,
      bytes
    };
  };

  const savePage = async ({ designKey, data, eTag }) => {
    if (!designKey || !data || !eTag) {
      fail("SAVE_PAGE_ARGUMENTS_MISSING", {
        hasDesignKey: !!designKey,
        hasData: !!data,
        hasETag: !!eTag
      });
    }

    const payload = {
      data,
      file: {
        isNew: false,
        eTag
      }
    };

    const compressed = await gzipJson(payload);

    const response = await fetch(
      `${API_BASE}/designs/${encodeURIComponent(designKey)}`,
      {
        method: "POST",
        mode: "cors",
        cache: "no-store",
        headers: authHeaders({
          "Content-Type": "application/json",
          "Content-Encoding": "gzip"
        }),
        body: compressed.bytes
      }
    );

    const text = await response.text();
    let result;

    try {
      result = JSON.parse(text);
    } catch {
      fail("SAVE_RESPONSE_NOT_JSON", {
        status: response.status,
        text: text.slice(0, 500)
      });
    }

    if (!response.ok || result.saved !== true) {
      fail("SHOWIT_SAVE_FAILED", {
        status: response.status,
        response: result
      });
    }

    const newETag = stripEtag(result.eTag);
    if (!newETag) fail("NEW_ETAG_MISSING", { result });
    if (newETag === eTag) fail("ETAG_DID_NOT_CHANGE", { eTag, newETag });

    return {
      saved: true,
      oldETag: eTag,
      newETag,
      rawJsonBytes: compressed.rawJsonBytes,
      gzipBytes: compressed.gzipBytes,
      response: result
    };
  };

  const readImageDimensions = file =>
    new Promise((resolve, reject) => {
      const url = URL.createObjectURL(file);
      const img = new Image();

      img.onload = () => {
        const value = {
          width: img.naturalWidth,
          height: img.naturalHeight
        };
        URL.revokeObjectURL(url);
        resolve(value);
      };

      img.onerror = () => {
        URL.revokeObjectURL(url);
        reject(new Error("IMAGE_DIMENSION_READ_FAILED"));
      };

      img.src = url;
    });

  const pickImages = ({ multiple = true, accept = "image/jpeg,image/png" } = {}) =>
    new Promise((resolve, reject) => {
      const old = document.getElementById("__showit_compiler_file_picker__");
      if (old) old.remove();

      const overlay = document.createElement("div");
      overlay.id = "__showit_compiler_file_picker__";
      Object.assign(overlay.style, {
        position: "fixed",
        left: "50%",
        top: "50%",
        transform: "translate(-50%, -50%)",
        zIndex: "2147483647",
        background: "#111",
        color: "#fff",
        padding: "28px",
        borderRadius: "12px",
        fontFamily: "Arial, sans-serif",
        boxShadow: "0 10px 50px rgba(0,0,0,.6)",
        textAlign: "center",
        minWidth: "340px"
      });

      const title = document.createElement("div");
      title.textContent = "SHOWIT PAGE COMPILER V1";
      title.style.fontSize = "16px";
      title.style.marginBottom = "10px";

      const note = document.createElement("div");
      note.textContent = multiple
        ? "Choose one or more JPG/PNG files from your computer."
        : "Choose one JPG/PNG file from your computer.";
      note.style.fontSize = "13px";
      note.style.marginBottom = "18px";
      note.style.opacity = "0.8";

      const input = document.createElement("input");
      input.type = "file";
      input.accept = accept;
      input.multiple = multiple;
      input.style.display = "block";
      input.style.margin = "0 auto";
      input.style.background = "#fff";
      input.style.color = "#000";
      input.style.padding = "12px";

      const cancel = document.createElement("button");
      cancel.textContent = "Cancel";
      cancel.style.marginTop = "14px";
      cancel.style.padding = "8px 14px";
      cancel.onclick = () => {
        overlay.remove();
        reject(new Error("FILE_PICK_CANCELLED"));
      };

      input.onchange = () => {
        const files = Array.from(input.files || []);
        overlay.remove();
        if (!files.length) {
          reject(new Error("NO_FILE_SELECTED"));
          return;
        }
        resolve(files);
      };

      overlay.append(title, note, input, cancel);
      document.body.appendChild(overlay);
    });

  const uploadImage = async (file, { folderId = null } = {}) => {
    if (!(file instanceof File)) {
      fail("UPLOAD_REQUIRES_FILE_OBJECT");
    }

    if (!["image/jpeg", "image/png"].includes(file.type)) {
      fail("UNSUPPORTED_FILE_TYPE", { name: file.name, type: file.type });
    }

    const dimensions = await readImageDimensions(file);

    const createResponse = await fetch(`${API_BASE}/useruploads`, {
      method: "POST",
      mode: "cors",
      cache: "no-store",
      headers: authHeaders({ "Content-Type": "application/json" }),
      body: JSON.stringify({
        filename: file.name,
        size: file.size,
        width: dimensions.width,
        height: dimensions.height,
        folder_id: folderId
      })
    });

    const createText = await createResponse.text();
    let created;

    try {
      created = JSON.parse(createText);
    } catch {
      fail("CREATE_UPLOAD_RESPONSE_NOT_JSON", {
        status: createResponse.status,
        text: createText.slice(0, 500)
      });
    }

    if (!createResponse.ok || created.status !== 200) {
      fail("CREATE_UPLOAD_FAILED", {
        status: createResponse.status,
        response: created,
        filename: file.name
      });
    }

    const asset = created.asset;
    const upload = created.upload;

    if (!asset?.asset_id || !asset?.key || !upload?.url || !upload?.upload_id) {
      fail("CREATE_UPLOAD_SCHEMA_UNEXPECTED", { created });
    }

    const putHeaders = { ...(upload.headers || {}) };
    if (!putHeaders["Content-Type"] && !putHeaders["content-type"]) {
      putHeaders["Content-Type"] = file.type;
    }

    const putResponse = await fetch(upload.url, {
      method: "PUT",
      mode: "cors",
      headers: putHeaders,
      body: file
    });

    if (!putResponse.ok) {
      fail("S3_PUT_FAILED", {
        status: putResponse.status,
        statusText: putResponse.statusText,
        filename: file.name,
        uploadId: upload.upload_id
      });
    }

    const completeResponse = await fetch(
      `${API_BASE}/useruploads/${encodeURIComponent(upload.upload_id)}/complete`,
      {
        method: "POST",
        mode: "cors",
        cache: "no-store",
        headers: authHeaders({ "Content-Type": "application/json" }),
        body: "{}"
      }
    );

    const completeText = await completeResponse.text();
    let completed;

    try {
      completed = JSON.parse(completeText);
    } catch {
      fail("COMPLETE_RESPONSE_NOT_JSON", {
        status: completeResponse.status,
        text: completeText.slice(0, 500)
      });
    }

    if (!completeResponse.ok || completed.status !== 1) {
      fail("UPLOAD_COMPLETE_FAILED", {
        status: completeResponse.status,
        response: completed,
        filename: file.name,
        uploadId: upload.upload_id
      });
    }

    if (completed.asset_id !== asset.asset_id) {
      fail("ASSET_ID_MISMATCH", {
        createdAssetId: asset.asset_id,
        completedAssetId: completed.asset_id
      });
    }

    const normalized = {
      asset_id: asset.asset_id,
      user_id: asset.user_id,
      file_id: completed.file_id || asset.file_id || "",
      filename: asset.filename,
      asset_name: asset.asset_name,
      aspect_ratio: asset.aspect_ratio,
      width: asset.width || dimensions.width,
      height: asset.height || dimensions.height,
      key: asset.key,
      upload_id: upload.upload_id,
      content_type: file.type,
      original_name: file.name,
      size: file.size,
      preview_url: `https://static.showit.com/v2/${encodeURIComponent(
        asset.user_id
      )}/${encodeURIComponent(asset.asset_id)}/${encodeURIComponent(asset.filename)}/preview`
    };

    return normalized;
  };

  const uploadImages = async (files, options = {}) => {
    const list = Array.from(files || []);
    if (!list.length) return [];

    const results = [];
    for (const file of list) {
      results.push(await uploadImage(file, options));
    }
    return results;
  };

  const assetToGraphicContent = asset => {
    if (!asset?.key || typeof asset?.aspect_ratio !== "number") {
      fail("INVALID_ASSET_FOR_GRAPHIC", { asset });
    }

    return {
      key: asset.key,
      aspect_ratio: asset.aspect_ratio,
      title: asset.asset_name || asset.title || asset.filename || "image",
      type: "asset"
    };
  };

  const normalizeBox = (box = {}, defaults = {}) => ({
    w: box.w ?? defaults.w,
    h: box.h ?? defaults.h,
    x: box.x ?? defaults.x ?? 0,
    y: box.y ?? defaults.y ?? 0,
    a: box.a ?? defaults.a ?? 0,
    ...(box.size != null ? { size: box.size } : {}),
    ...(box.c != null ? { c: box.c } : {}),
    ...(box.lS != null ? { lS: box.lS } : {}),
    ...(box.lH != null ? { lH: box.lH } : {}),
    ...(box.style != null ? { style: box.style } : {})
  });

  const createText = spec => {
    if (!spec?.text) fail("TEXT_VALUE_REQUIRED", { spec });

    const desktop = normalizeBox(spec.desktop, {
      w: 600,
      h: 80,
      x: 60,
      y: 60,
      a: 0
    });

    const mobile = normalizeBox(spec.mobile, {
      w: 280,
      h: 80,
      x: 20,
      y: 40,
      a: 0
    });

    desktop.size = spec.desktop?.size ?? spec.size ?? 24;
    desktop.c = spec.desktop?.c ?? spec.color ?? "#111111:100";
    desktop.lS = spec.desktop?.lS ?? spec.letterSpacing ?? 0;
    desktop.lH = spec.desktop?.lH ?? spec.lineHeight ?? 1.2;
    desktop.style = spec.desktop?.style ?? spec.style ?? "paragraph";

    if (mobile.size == null) mobile.size = spec.mobile?.size ?? spec.size ?? 20;

    return {
      type: "text",
      visible: spec.visible ?? "a",
      content: {
        text: spec.text,
        sample:
          spec.sample ??
          String(spec.text)
            .replace(/<br\s*\/?>/gi, " ")
            .replace(/<[^>]+>/g, "")
            .slice(0, 80)
      },
      mobile,
      desktop,
      style: spec.style ?? "paragraph",
      sync:
        spec.sync ??
        [
          "style",
          "over",
          "o",
          "blur",
          "border.rad",
          "shadow.style",
          "trIn.type",
          "lH",
          "lS",
          "c"
        ]
    };
  };

  const createImage = spec => {
    const desktop = normalizeBox(spec?.desktop, {
      w: 320,
      h: 420,
      x: 800,
      y: 80,
      a: 0
    });

    const mobile = normalizeBox(spec?.mobile, {
      w: 280,
      h: 200,
      x: 20,
      y: 300,
      a: 0
    });

    const content = spec?.asset
      ? assetToGraphicContent(spec.asset)
      : spec?.content
      ? clone(spec.content)
      : {};

    return {
      type: "graphic",
      visible: spec?.visible ?? "a",
      content,
      mobile,
      desktop,
      sync:
        spec?.sync ??
        ["gs.t", "o", "blur", "border.rad", "shadow.style", "trIn.type"]
    };
  };

  const createCanvas = (spec, existingBlockData = {}) => {
    if (!spec?.name) fail("CANVAS_NAME_REQUIRED", { spec });

    const id = spec.id || makeId(existingBlockData);
    const slug =
      spec.slug ||
      String(spec.name)
        .trim()
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-+|-+$/g, "") ||
      `canvas-${id}`;

    const elements = (spec.elements || []).map(element => {
      if (element?.type === "text") return createText(element);
      if (element?.type === "image" || element?.type === "graphic") {
        return createImage(element);
      }
      fail("UNSUPPORTED_ELEMENT_TYPE", {
        canvas: spec.name,
        elementType: element?.type
      });
    });

    return {
      id,
      block: {
        mobile: {
          w: spec.mobile?.w ?? 320,
          h: spec.mobile?.h ?? 620,
          bgMediaType: "none",
          bgFillType: "color",
          bgColor: spec.mobile?.bgColor ?? spec.background ?? "#ffffff:100"
        },
        states: clone(spec.states || []),
        name: spec.name,
        slug,
        visible: spec.visible ?? "a",
        elements,
        type: "block",
        id,
        sync:
          spec.sync ??
          [
            "bgFillType",
            "bgMediaType",
            "stateTrIn.type",
            "stateTrOut.type",
            "trIn.type",
            "trOut.type"
          ],
        desktop: {
          w: spec.desktop?.w ?? 1200,
          h: spec.desktop?.h ?? 620,
          bgMediaType: "none",
          bgFillType: "color",
          bgColor: spec.desktop?.bgColor ?? spec.background ?? "#ffffff:100"
        }
      }
    };
  };

  const findCanvasIdByName = (data, name) => {
    const hits = data.blocks.filter(id => data.blockData[id]?.name === name);
    if (hits.length !== 1) {
      fail("CANVAS_MATCH_FAILED", { name, count: hits.length });
    }
    return hits[0];
  };

  const waitForDurablePage = async ({ expectedETag, validate, attempts = 15 }) => {
    let lastSeen = null;

    for (let attempt = 1; attempt <= attempts; attempt++) {
      await sleep(attempt === 1 ? 350 : 750);
      const fresh = await loadPage();
      lastSeen = { attempt, eTag: fresh.eTag };

      if (fresh.eTag !== expectedETag) continue;

      const validation = await validate(fresh, attempt);
      if (validation?.ok) {
        return {
          attempt,
          page: fresh,
          validation
        };
      }

      lastSeen = {
        ...lastSeen,
        validation
      };
    }

    fail("DURABLE_READBACK_FAILED", {
      expectedETag,
      lastSeen
    });
  };

  const buildPage = async ({
    anchorName,
    canvases,
    position = "after",
    verifyUnchanged = true
  } = {}) => {
    if (!anchorName) fail("ANCHOR_NAME_REQUIRED");
    if (!Array.isArray(canvases) || !canvases.length) {
      fail("CANVASES_REQUIRED");
    }
    if (!["after", "before"].includes(position)) {
      fail("INVALID_INSERT_POSITION", { position });
    }

    const loaded = await loadPage();
    const data = loaded.data;
    const oldETag = loaded.eTag;

    const requestedNames = canvases.map(canvas => canvas?.name).filter(Boolean);
    if (requestedNames.length !== canvases.length) {
      fail("EVERY_CANVAS_NEEDS_NAME");
    }

    const duplicateRequested = requestedNames.filter(
      (name, index) => requestedNames.indexOf(name) !== index
    );
    if (duplicateRequested.length) {
      fail("DUPLICATE_REQUESTED_CANVAS_NAMES", {
        names: [...new Set(duplicateRequested)]
      });
    }

    const existingCollisions = data.blocks
      .map(id => ({ id, name: data.blockData[id]?.name }))
      .filter(item => requestedNames.includes(item.name));

    if (existingCollisions.length) {
      fail("CANVAS_NAME_COLLISION", { collisions: existingCollisions });
    }

    const anchorId = findCanvasIdByName(data, anchorName);
    const anchorIndex = data.blocks.indexOf(anchorId);

    const beforeOrder = [...data.blocks];
    const beforeBlocks = {};
    for (const id of beforeOrder) {
      beforeBlocks[id] = stableStringify(data.blockData[id]);
    }

    const beforeMeta = clone(data);
    delete beforeMeta.blocks;
    delete beforeMeta.blockData;
    const beforeMetaSnapshot = stableStringify(beforeMeta);

    const created = [];

    for (const spec of canvases) {
      const compiled = createCanvas(spec, data.blockData);
      if (data.blockData[compiled.id]) {
        fail("GENERATED_BLOCK_ID_COLLISION", { id: compiled.id });
      }
      data.blockData[compiled.id] = compiled.block;
      created.push({
        id: compiled.id,
        name: compiled.block.name,
        slug: compiled.block.slug,
        elementCount: compiled.block.elements.length,
        elementTypes: compiled.block.elements.map(element => element.type)
      });
    }

    const insertAt = position === "after" ? anchorIndex + 1 : anchorIndex;
    data.blocks.splice(insertAt, 0, ...created.map(item => item.id));

    const localOrder = data.blocks.slice(insertAt, insertAt + created.length);
    if (stableStringify(localOrder) !== stableStringify(created.map(item => item.id))) {
      fail("LOCAL_ORDER_VERIFY_FAILED", {
        expected: created.map(item => item.id),
        actual: localOrder
      });
    }

    const save = await savePage({
      designKey: loaded.designKey,
      data,
      eTag: oldETag
    });

    const readback = await waitForDurablePage({
      expectedETag: save.newETag,
      validate: fresh => {
        const actualIds = fresh.data.blocks.slice(insertAt, insertAt + created.length);
        if (
          stableStringify(actualIds) !==
          stableStringify(created.map(item => item.id))
        ) {
          return {
            ok: false,
            reason: "CREATED_BLOCK_ORDER_MISMATCH",
            actualIds
          };
        }

        for (const item of created) {
          const block = fresh.data.blockData[item.id];
          if (!block) {
            return { ok: false, reason: "CREATED_BLOCK_MISSING", item };
          }
          if (
            block.name !== item.name ||
            block.slug !== item.slug ||
            block.elements?.length !== item.elementCount
          ) {
            return {
              ok: false,
              reason: "CREATED_BLOCK_SHAPE_MISMATCH",
              item,
              actual: {
                name: block.name,
                slug: block.slug,
                elementCount: block.elements?.length
              }
            };
          }
        }

        if (verifyUnchanged) {
          const oldOrder = fresh.data.blocks.filter(
            id => !created.some(item => item.id === id)
          );

          if (stableStringify(oldOrder) !== stableStringify(beforeOrder)) {
            fail("OLD_BLOCK_ORDER_CHANGED", { beforeOrder, oldOrder });
          }

          for (const id of beforeOrder) {
            const after = stableStringify(fresh.data.blockData[id]);
            if (after !== beforeBlocks[id]) {
              fail("OLD_BLOCK_MUTATED", {
                id,
                name: fresh.data.blockData[id]?.name
              });
            }
          }

          const freshMeta = clone(fresh.data);
          delete freshMeta.blocks;
          delete freshMeta.blockData;
          if (stableStringify(freshMeta) !== beforeMetaSnapshot) {
            fail("PAGE_METADATA_CHANGED");
          }
        }

        return {
          ok: true,
          createdCount: created.length,
          createdElementCount: created.reduce((sum, item) => sum + item.elementCount, 0),
          totalBlocks: fresh.data.blocks.length
        };
      }
    });

    return {
      status: "SHOWIT_PAGE_BUILD_SAVED_AND_READBACK_VERIFIED",
      compilerVersion: VERSION,
      designKey: loaded.designKey,
      pageId: loaded.pageId,
      anchorName,
      position,
      created,
      oldETag,
      newETag: save.newETag,
      pageSaveCount: 1,
      rawJsonBytes: save.rawJsonBytes,
      gzipBytes: save.gzipBytes,
      durableReadbackAttempt: readback.attempt,
      verification: readback.validation
    };
  };

  const api = Object.freeze({
    VERSION,
    info: () => ({
      name: GLOBAL_NAME,
      version: VERSION,
      status: "CANDIDATE / LIVE-PROVEN PRIMITIVES",
      capabilities: [
        "load current Showit page + ETag",
        "direct authenticated whole-page save",
        "local image upload to Showit",
        "text element compilation",
        "image/graphic element compilation",
        "Canvas compilation",
        "multi-Canvas one-save build",
        "durable readback with unchanged-old-state verification"
      ]
    }),
    discoverCurrentPage,
    loadPage,
    savePage,
    pickImages,
    uploadImage,
    uploadImages,
    assetToGraphicContent,
    createText,
    createImage,
    createCanvas,
    buildPage
  });

  globalThis[GLOBAL_NAME] = api;

  const installed = api.info();
  console.log("SHOWIT_PAGE_COMPILER_V1_INSTALLED", installed);
  return installed;
})();
