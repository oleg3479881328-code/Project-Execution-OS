// Showit Page Compiler v1 — integrated acceptance v2
// Fix: load canonical module through Playwright APIRequestContext instead of bare fetch in Dramaturg runtime.

(async () => {
  const MODULE_URL = "https://raw.githubusercontent.com/oleg3479881328-code/Project-Execution-OS/main/projects/website-creation/adapters/showit/showit-page-compiler-v1.js";

  const requestContext = page.request || page.context()?.request;
  if (!requestContext || typeof requestContext.get !== "function") {
    throw new Error("PLAYWRIGHT_REQUEST_CONTEXT_UNAVAILABLE");
  }

  const moduleResponse = await requestContext.get(
    `${MODULE_URL}?t=${Date.now()}`,
    { timeout: 20000 }
  );

  if (!moduleResponse.ok()) {
    throw new Error(
      `COMPILER_SOURCE_LOAD_FAILED ${JSON.stringify({
        status: moduleResponse.status(),
        statusText: moduleResponse.statusText()
      })}`
    );
  }

  const moduleSource = await moduleResponse.text();

  const installed = await page.evaluate(source => (0, eval)(source), moduleSource);
  if (!installed || !String(installed.version || "").startsWith("1.0.0")) {
    throw new Error(`COMPILER_INSTALL_FAILED ${JSON.stringify({ installed })}`);
  }

  const acceptance = await page.evaluate(async () => {
    const c = globalThis.ShowitPageCompilerV1;
    if (!c) throw new Error("COMPILER_GLOBAL_MISSING");

    const before = await c.loadPage();
    const anchorCandidates = [
      "API PAGE — CTA",
      "API TEST — CREATED FROM SCRATCH",
      "IRONLINE — FINAL"
    ];

    const anchorName = anchorCandidates.find(name =>
      before.data.blocks.some(id => before.data.blockData[id]?.name === name)
    );

    if (!anchorName) {
      throw new Error(`ACCEPTANCE_ANCHOR_NOT_FOUND ${JSON.stringify({
        tried: anchorCandidates,
        available: before.data.blocks.map(id => before.data.blockData[id]?.name).filter(Boolean)
      })}`);
    }

    const files = await c.pickImages({ multiple: false });
    const file = files[0];
    if (!file) throw new Error("ACCEPTANCE_FILE_MISSING");

    const asset = await c.uploadImage(file);
    if (!asset?.asset_id || !asset?.key || typeof asset?.aspect_ratio !== "number") {
      throw new Error(`ACCEPTANCE_UPLOAD_RESULT_INVALID ${JSON.stringify({ asset })}`);
    }

    const stamp = Date.now().toString().slice(-8);
    const heroName = `COMPILER V1 ACCEPT — HERO — ${stamp}`;
    const imageName = `COMPILER V1 ACCEPT — IMAGE — ${stamp}`;

    const build = await c.buildPage({
      anchorName,
      position: "after",
      verifyUnchanged: true,
      canvases: [
        {
          name: heroName,
          slug: `compiler-v1-accept-hero-${stamp}`,
          background: "#111111:100",
          desktop: { w: 1200, h: 620 },
          mobile: { w: 320, h: 620 },
          elements: [
            {
              type: "text",
              text: "SHOWIT PAGE COMPILER V1",
              color: "#f2c500:100",
              desktop: { x: 60, y: 70, w: 700, h: 50, size: 18 },
              mobile: { x: 20, y: 50, w: 280, h: 45, size: 14 }
            },
            {
              type: "text",
              text: "ONE MODULE.<br>ONE PAGE SAVE.",
              color: "#f3f0e8:100",
              desktop: { x: 60, y: 155, w: 780, h: 180, size: 64 },
              mobile: { x: 20, y: 125, w: 280, h: 150, size: 38 }
            },
            {
              type: "text",
              text: "INTEGRATED ACCEPTANCE RUN",
              color: "#f3f0e8:100",
              desktop: { x: 60, y: 420, w: 520, h: 50, size: 18 },
              mobile: { x: 20, y: 390, w: 280, h: 55, size: 15 }
            }
          ]
        },
        {
          name: imageName,
          slug: `compiler-v1-accept-image-${stamp}`,
          background: "#f3f0e8:100",
          desktop: { w: 1200, h: 700 },
          mobile: { w: 320, h: 700 },
          elements: [
            {
              type: "text",
              text: "LOCAL FILE → SHOWIT ASSET → CANVAS",
              color: "#111111:100",
              desktop: { x: 60, y: 70, w: 680, h: 80, size: 36 },
              mobile: { x: 20, y: 45, w: 280, h: 100, size: 28 }
            },
            {
              type: "image",
              asset,
              desktop: { x: 700, y: 90, w: 380, h: 500 },
              mobile: { x: 20, y: 220, w: 280, h: 400 }
            },
            {
              type: "text",
              text: `FILE: ${asset.original_name || asset.filename}`,
              color: "#111111:100",
              desktop: { x: 60, y: 250, w: 520, h: 60, size: 18 },
              mobile: { x: 20, y: 160, w: 280, h: 45, size: 14 }
            }
          ]
        }
      ]
    });

    if (build?.status !== "SHOWIT_PAGE_BUILD_SAVED_AND_READBACK_VERIFIED") {
      throw new Error(`ACCEPTANCE_BUILD_STATUS_FAILED ${JSON.stringify({ build })}`);
    }
    if (build.pageSaveCount !== 1) {
      throw new Error(`ACCEPTANCE_PAGE_SAVE_COUNT_FAILED ${JSON.stringify({ pageSaveCount: build.pageSaveCount })}`);
    }

    const readback = await c.loadPage();
    const getBlockByName = name => {
      const hits = readback.data.blocks.filter(id => readback.data.blockData[id]?.name === name);
      if (hits.length !== 1) {
        throw new Error(`ACCEPTANCE_READBACK_CANVAS_MATCH_FAILED ${JSON.stringify({ name, count: hits.length })}`);
      }
      return readback.data.blockData[hits[0]];
    };

    const heroBlock = getBlockByName(heroName);
    const imageBlock = getBlockByName(imageName);
    const graphics = (imageBlock.elements || []).filter(el => el?.type === "graphic");
    if (graphics.length !== 1) {
      throw new Error(`ACCEPTANCE_IMAGE_GRAPHIC_COUNT_FAILED ${JSON.stringify({ count: graphics.length })}`);
    }

    const graphicContent = graphics[0].content || {};
    if (
      graphicContent.type !== "asset" ||
      graphicContent.key !== asset.key ||
      graphicContent.aspect_ratio !== asset.aspect_ratio
    ) {
      throw new Error(`ACCEPTANCE_IMAGE_BINDING_READBACK_FAILED ${JSON.stringify({
        expected: c.assetToGraphicContent(asset),
        actual: graphicContent
      })}`);
    }

    return {
      status: "SHOWIT_PAGE_COMPILER_V1_INTEGRATED_READBACK_VERIFIED",
      compiler: c.info(),
      anchorName,
      selectedFile: { name: file.name, type: file.type, size: file.size },
      uploadedAsset: {
        asset_id: asset.asset_id,
        filename: asset.filename,
        key: asset.key,
        aspect_ratio: asset.aspect_ratio,
        upload_id: asset.upload_id,
        file_id: asset.file_id
      },
      createdCanvases: { heroName, imageName },
      build,
      independentReadback: {
        eTag: readback.eTag,
        heroElementCount: heroBlock.elements?.length,
        imageElementCount: imageBlock.elements?.length,
        imageGraphicContent: graphicContent
      }
    };
  });

  await page.reload({ waitUntil: "domcontentloaded", timeout: 60000 });
  await page.waitForTimeout(5000);

  const heroLocator = page.getByText(acceptance.createdCanvases.heroName, { exact: true });
  const imageLocator = page.getByText(acceptance.createdCanvases.imageName, { exact: true });
  const heroCanvasCount = await heroLocator.count().catch(() => -1);
  const imageCanvasCount = await imageLocator.count().catch(() => -1);

  if (imageCanvasCount > 0) {
    await imageLocator.first().click().catch(() => {});
    await page.waitForTimeout(2000);
  }

  const finalResult = {
    ...acceptance,
    editorReloaded: true,
    ui: { heroCanvasCount, imageCanvasCount },
    finalStatus:
      heroCanvasCount === 1 && imageCanvasCount === 1
        ? "SHOWIT PAGE COMPILER V1 — INTEGRATED ACCEPTANCE READY FOR VISUAL QA"
        : "SHOWIT PAGE COMPILER V1 — DURABLE PASS / UI SIDEBAR CHECK INCOMPLETE"
  };

  console.log("SHOWIT_PAGE_COMPILER_V1_ACCEPTANCE_RESULT", finalResult);
  return finalResult;
})()
