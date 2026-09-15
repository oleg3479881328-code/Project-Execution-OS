import { expect, test } from '@playwright/test'

test('shared Website Creator editor loads, edits images, and draft/publish changes reach the public renderer', async ({ page }) => {
  const email = process.env.WC_ADMIN_EMAIL
  const password = process.env.WC_ADMIN_PASSWORD
  expect(email, 'WC_ADMIN_EMAIL must be set for editor E2E').toBeTruthy()
  expect(password, 'WC_ADMIN_PASSWORD must be set for editor E2E').toBeTruthy()

  await page.goto('/admin/login')
  await page.locator('#field-email').fill(email!)
  await page.locator('#field-password').fill(password!)
  await page.locator('form button[type="submit"]').click()
  await expect(page).not.toHaveURL(/\/admin\/login/, { timeout: 15_000 })

  await page.goto('/editor')
  await expect(page).toHaveURL(/\/admin\/puck-editor\/pages\/.+/, { timeout: 15_000 })
  await expect(page.getByRole('button', { name: /^Save$/ }).first()).toBeVisible({ timeout: 15_000 })
  await expect(page.getByRole('button', { name: /^Publish$/ }).first()).toBeVisible({ timeout: 15_000 })

  const match = page.url().match(/\/admin\/puck-editor\/pages\/([^/?#]+)/)
  expect(match?.[1]).toBeTruthy()
  const pageId = match![1]

  const readResponse = await page.request.get(`/api/puck/pages/${pageId}`)
  expect(readResponse.ok()).toBeTruthy()
  const readJson = await readResponse.json()
  const originalData = readJson.doc.puckData
  expect(originalData?.content?.length).toBeGreaterThan(0)

  const editorCanvas = page.frameLocator('iframe').first()
  await expect(editorCanvas.getByText('Diagnose. Repair. Drive.').first()).toBeVisible({ timeout: 15_000 })
  await expect(editorCanvas.getByText('Explore our services').first()).toBeVisible({ timeout: 15_000 })
  await expect(editorCanvas.locator('.wc-service-card__image')).toHaveCount(6)

  // Proven Olga image interaction contract, now generalized for Website Creator.
  const heroFrame = editorCanvas.locator('.wc-editable-image--hero .wc-image-frame').first()
  await expect(heroFrame).toBeVisible({ timeout: 15_000 })
  await heroFrame.click({ position: { x: 80, y: 80 } })
  await expect(editorCanvas.getByRole('toolbar', { name: 'Image controls' })).toBeVisible()
  await expect(editorCanvas.getByRole('button', { name: 'Replace photograph' })).toBeVisible()
  await expect(editorCanvas.getByRole('button', { name: /Crop \/ move photograph/ })).toBeVisible()

  const inspector = page.locator('[data-wc-image-inspector="hero"]')
  await expect(inspector).toBeVisible()
  await expect(inspector.getByText('Hero photograph')).toBeVisible()

  // Exercise sequential image edits. The photograph must remain selected after each atomic Puck update.
  const shape = inspector.locator('select').first()
  await expect(shape).toBeVisible()
  await shape.selectOption('square')
  await expect(heroFrame).toHaveAttribute('data-ratio', 'square')
  await shape.selectOption('portrait')
  await expect(heroFrame).toHaveAttribute('data-ratio', 'portrait')

  // Inspector and canvas toolbar must edit the same canonical image state.
  await inspector.getByRole('button', { name: 'Fit full photo' }).click()
  await expect(heroFrame).toHaveAttribute('data-fit', 'fit')
  await expect(inspector.getByText('Fit shows the full photograph. Switch to Fill to crop it.')).toBeVisible()
  await expect(editorCanvas.getByRole('button', { name: 'Fill frame / crop' })).toBeVisible()
  await editorCanvas.getByRole('button', { name: 'Fill frame / crop' }).click()
  await expect(heroFrame).toHaveAttribute('data-fit', 'fill')
  await expect(inspector.getByText('Use Crop / move photograph to open the focused crop dialog.')).toBeVisible()

  const ranges = inspector.locator('input[type="range"]')
  const zoom = ranges.nth(0)
  const focalX = ranges.nth(1)
  const focalY = ranges.nth(2)
  await zoom.fill('1.25')
  await expect(inspector.getByText('Zoom · 1.25×')).toBeVisible()
  await focalX.fill('35')
  await focalY.fill('65')
  await expect(inspector.getByText('Horizontal · 35%')).toBeVisible()
  await expect(inspector.getByText('Vertical · 65%')).toBeVisible()
  await inspector.getByRole('button', { name: 'Reset crop' }).click()
  await expect(heroFrame).toHaveAttribute('data-fit', 'fill')
  await expect(heroFrame).toHaveAttribute('data-crop', 'legacy')
  await expect(inspector.getByText('Zoom · 1.00×')).toBeVisible()
  await expect(inspector.getByText('Horizontal · 50%')).toBeVisible()
  await expect(inspector.getByText('Vertical · 50%')).toBeVisible()

  // Crop / move is library-backed and persists a percentage crop rectangle only on Apply.
  // The focused dialog is an editor-shell overlay, while the photograph itself remains in Puck's canvas iframe.
  await editorCanvas.getByRole('button', { name: 'Crop / move photograph' }).click()
  const cropDialog = page.getByRole('dialog', { name: 'Crop and move photograph' })
  await expect(cropDialog).toBeVisible()
  const cropZoom = cropDialog.getByRole('slider', { name: 'Crop zoom' })
  const zoomInCrop = cropDialog.getByRole('button', { name: 'Zoom in crop' })
  await zoomInCrop.click()
  await expect(cropDialog.getByText('Zoom · 1.10×')).toBeVisible()
  await cropDialog.getByRole('button', { name: 'Reset' }).click()
  await expect(cropDialog.getByText('Zoom · 1.00×')).toBeVisible()
  await cropZoom.fill('1.35')
  await expect(cropDialog.getByText('Zoom · 1.35×')).toBeVisible()
  await expect(cropDialog.getByRole('button', { name: 'Apply crop' })).toBeEnabled()
  await cropDialog.getByRole('button', { name: 'Apply crop' }).click()
  await expect(cropDialog).toHaveCount(0)
  await expect(heroFrame).toHaveAttribute('data-crop', 'precise')

  const firstSavedCrop = {
    x: await heroFrame.getAttribute('data-crop-x'),
    y: await heroFrame.getAttribute('data-crop-y'),
    width: await heroFrame.getAttribute('data-crop-width'),
    height: await heroFrame.getAttribute('data-crop-height'),
  }
  expect(firstSavedCrop.x).toBeTruthy()
  expect(firstSavedCrop.y).toBeTruthy()
  expect(firstSavedCrop.width).toBeTruthy()
  expect(firstSavedCrop.height).toBeTruthy()

  // Reopen must restore the exact saved percentage rectangle. Escape and Cancel must not mutate it.
  await editorCanvas.getByRole('button', { name: 'Crop / move photograph' }).click()
  await expect(cropDialog).toBeVisible()
  await expect(cropDialog.getByText('Saved crop restored. Drag the photograph or adjust zoom.')).toBeVisible()
  await expect(cropDialog).toHaveAttribute('data-initial-crop-x', firstSavedCrop.x!)
  await expect(cropDialog).toHaveAttribute('data-initial-crop-y', firstSavedCrop.y!)
  await expect(cropDialog).toHaveAttribute('data-initial-crop-width', firstSavedCrop.width!)
  await expect(cropDialog).toHaveAttribute('data-initial-crop-height', firstSavedCrop.height!)
  await page.keyboard.press('Escape')
  await expect(cropDialog).toHaveCount(0)
  await expect(heroFrame).toHaveAttribute('data-crop-x', firstSavedCrop.x!)
  await expect(heroFrame).toHaveAttribute('data-crop-y', firstSavedCrop.y!)

  await editorCanvas.getByRole('button', { name: 'Crop / move photograph' }).click()
  await expect(cropDialog).toBeVisible()
  await cropDialog.getByRole('button', { name: 'Cancel', exact: true }).click()
  await expect(cropDialog).toHaveCount(0)
  await expect(heroFrame).toHaveAttribute('data-crop-x', firstSavedCrop.x!)
  await expect(heroFrame).toHaveAttribute('data-crop-y', firstSavedCrop.y!)

  // Reset must clear a precise crop back to the default/legacy semantics.
  await inspector.getByRole('button', { name: 'Reset crop' }).click()
  await expect(heroFrame).toHaveAttribute('data-crop', 'legacy')

  // Create a fresh precise crop, move the photograph with a real pointer drag,
  // then prove that moved semantic crop survives Save → reload → Publish.
  await editorCanvas.getByRole('button', { name: 'Crop / move photograph' }).click()
  await expect(cropDialog).toBeVisible()
  await cropDialog.getByRole('slider', { name: 'Crop zoom' }).fill('1.3')
  await expect(cropDialog.getByText('Zoom · 1.30×')).toBeVisible()
  await expect(cropDialog.getByRole('button', { name: 'Apply crop' })).toBeEnabled()

  const cropStage = cropDialog.getByTestId('wc-crop-stage')
  const stageBox = await cropStage.boundingBox()
  expect(stageBox).toBeTruthy()
  const dragStartX = stageBox!.x + stageBox!.width * 0.5
  const dragStartY = stageBox!.y + stageBox!.height * 0.5
  await page.mouse.move(dragStartX, dragStartY)
  await page.mouse.down()
  await page.mouse.move(
    dragStartX + Math.min(90, stageBox!.width * 0.18),
    dragStartY + Math.min(45, stageBox!.height * 0.1),
    { steps: 10 },
  )
  await page.mouse.up()

  await cropDialog.getByRole('button', { name: 'Apply crop' }).click()
  await expect(cropDialog).toHaveCount(0)
  await expect(heroFrame).toHaveAttribute('data-crop', 'precise')

  const savedCrop = {
    x: await heroFrame.getAttribute('data-crop-x'),
    y: await heroFrame.getAttribute('data-crop-y'),
    width: await heroFrame.getAttribute('data-crop-width'),
    height: await heroFrame.getAttribute('data-crop-height'),
  }
  expect(savedCrop.x).toBeTruthy()
  expect(savedCrop.y).toBeTruthy()
  expect(savedCrop.width).toBeTruthy()
  expect(savedCrop.height).toBeTruthy()

  // A centered percentage crop has a 50/50 center. A real drag must move the
  // persisted semantic rectangle away from that center on at least one axis.
  const savedCropCenterX = Number(savedCrop.x) + Number(savedCrop.width) / 2
  const savedCropCenterY = Number(savedCrop.y) + Number(savedCrop.height) / 2
  expect(
    Math.abs(savedCropCenterX - 50) > 0.25
      || Math.abs(savedCropCenterY - 50) > 0.25,
  ).toBeTruthy()

  // Alt text and caption/credit are ordinary canonical image properties. They
  // must ride the same owner Save/reload/Publish lifecycle as the moved crop.
  const savedAlt = 'Website Creator acceptance mechanic photograph'
  const savedCaption = 'Website Creator acceptance image credit'
  await inspector.getByLabel('Alt text').fill(savedAlt)
  await inspector.getByLabel('Caption / credit').fill(savedCaption)
  await expect(heroFrame.locator('img')).toHaveAttribute('alt', savedAlt)
  await expect(editorCanvas.getByText(savedCaption)).toBeVisible()

  const saveResponsePromise = page.waitForResponse((response) => (
    response.url().includes(`/api/puck/pages/${pageId}`)
    && response.request().method() === 'PATCH'
  ))
  await page.getByRole('button', { name: /^Save$/ }).first().click()
  const saveResponse = await saveResponsePromise
  expect(saveResponse.ok()).toBeTruthy()
  const saveBody = JSON.parse(saveResponse.request().postData() || '{}')
  expect(saveBody.draft).toBe(true)
  await expect(page.getByText('Unpublished Changes').first()).toBeVisible({ timeout: 10_000 })

  await page.reload()
  await expect(page).toHaveURL(/\/admin\/puck-editor\/pages\/.+/, { timeout: 15_000 })
  await expect(heroFrame).toBeVisible({ timeout: 15_000 })
  await expect(heroFrame).toHaveAttribute('data-crop', 'precise')
  await expect(heroFrame).toHaveAttribute('data-crop-x', savedCrop.x!)
  await expect(heroFrame).toHaveAttribute('data-crop-y', savedCrop.y!)
  await expect(heroFrame).toHaveAttribute('data-crop-width', savedCrop.width!)
  await expect(heroFrame).toHaveAttribute('data-crop-height', savedCrop.height!)
  await expect(heroFrame.locator('img')).toHaveAttribute('alt', savedAlt)
  await expect(editorCanvas.getByText(savedCaption)).toBeVisible()

  // Save is draft-only: public rendering must still expose the previous published image state and metadata.
  await page.goto('/')
  const publicHero = page.locator('.wc-public-image.wc-hero__image').first()
  const publicHeroFrame = publicHero.locator('.wc-public-image__frame')
  await expect(publicHeroFrame).toBeVisible({ timeout: 10_000 })
  await expect(publicHeroFrame).toHaveAttribute('data-crop', 'legacy')
  await expect(publicHero.locator('img')).not.toHaveAttribute('alt', savedAlt)
  await expect(page.getByText(savedCaption)).toHaveCount(0)

  // Reopen the editor draft and publish through the integration's real owner-facing control.
  await page.goto('/editor')
  await expect(page).toHaveURL(/\/admin\/puck-editor\/pages\/.+/, { timeout: 15_000 })
  await expect(heroFrame).toBeVisible({ timeout: 15_000 })
  await expect(heroFrame).toHaveAttribute('data-crop', 'precise')
  await expect(heroFrame).toHaveAttribute('data-crop-x', savedCrop.x!)
  await expect(heroFrame.locator('img')).toHaveAttribute('alt', savedAlt)
  await expect(editorCanvas.getByText(savedCaption)).toBeVisible()

  const publishResponsePromise = page.waitForResponse((response) => (
    response.url().includes(`/api/puck/pages/${pageId}`)
    && response.request().method() === 'PATCH'
  ))
  await page.getByRole('button', { name: /^Publish$/ }).first().click()
  const publishResponse = await publishResponsePromise
  expect(publishResponse.ok()).toBeTruthy()
  const publishBody = JSON.parse(publishResponse.request().postData() || '{}')
  expect(publishBody._status).toBe('published')
  await expect(page.getByText('Published').first()).toBeVisible({ timeout: 10_000 })

  await page.goto('/')
  await expect(publicHeroFrame).toBeVisible({ timeout: 10_000 })
  await expect(publicHeroFrame).toHaveAttribute('data-crop', 'precise')
  await expect(publicHeroFrame).toHaveAttribute('data-crop-x', savedCrop.x!)
  await expect(publicHeroFrame).toHaveAttribute('data-crop-y', savedCrop.y!)
  await expect(publicHeroFrame).toHaveAttribute('data-crop-width', savedCrop.width!)
  await expect(publicHeroFrame).toHaveAttribute('data-crop-height', savedCrop.height!)
  await expect(publicHero.locator('img')).toHaveAttribute('alt', savedAlt)
  await expect(publicHero.getByText(savedCaption)).toBeVisible()

  // Restore the canonical seeded published state so the acceptance remains repeatable.
  const restoreResponse = await page.request.patch(`/api/puck/pages/${pageId}`, {
    data: { puckData: originalData, _status: 'published' },
  })
  expect(restoreResponse.ok()).toBeTruthy()

  await page.goto('/')
  await expect(page.getByText('Clear answers before parts get replaced. Diagnostics, maintenance and major mechanical work for the cars you depend on.')).toBeVisible()
  await expect(publicHeroFrame).toHaveAttribute('data-crop', 'legacy')
  await expect(page.getByText(savedCaption)).toHaveCount(0)

  const versionsResponse = await page.request.get(`/api/puck/pages/${pageId}/versions?limit=5`)
  expect(versionsResponse.status()).not.toBe(404)
  expect(versionsResponse.ok()).toBeTruthy()

  // Replace remains a contextual toolbar action, but delegates selection/upload to the proven Payload media picker.
  await page.goto('/editor')
  await expect(page).toHaveURL(/\/admin\/puck-editor\/pages\/.+/, { timeout: 15_000 })
  await expect(heroFrame).toBeVisible({ timeout: 15_000 })
  await heroFrame.click({ position: { x: 80, y: 80 } })
  await expect(editorCanvas.getByRole('toolbar', { name: 'Image controls' })).toBeVisible()
  await editorCanvas.getByRole('button', { name: 'Replace photograph' }).click()
  const mediaHeading = page.getByRole('heading', { name: 'Select Media' })
  await expect(mediaHeading).toBeVisible({ timeout: 5_000 })
  await expect(page.getByRole('button', { name: 'Upload New' })).toBeVisible()
  await mediaHeading.locator('..').locator('button').click()
  await expect(mediaHeading).toHaveCount(0)

  await page.screenshot({ path: 'test-results/website-creator-editor.png', fullPage: true })
})