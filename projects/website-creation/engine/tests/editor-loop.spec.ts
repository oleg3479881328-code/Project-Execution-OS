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
  await expect(page.getByRole('button', { name: /Publish/i }).first()).toBeVisible({ timeout: 15_000 })

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

  // Reopen must restore the exact saved percentage rectangle. Escape and Cancel must not mutate it.
  await editorCanvas.getByRole('button', { name: 'Crop / move photograph' }).click()
  await expect(cropDialog).toBeVisible()
  await expect(cropDialog.getByText('Saved crop restored. Drag the photograph or adjust zoom.')).toBeVisible()
  await expect(cropDialog).toHaveAttribute('data-initial-crop-x', savedCrop.x!)
  await expect(cropDialog).toHaveAttribute('data-initial-crop-y', savedCrop.y!)
  await expect(cropDialog).toHaveAttribute('data-initial-crop-width', savedCrop.width!)
  await expect(cropDialog).toHaveAttribute('data-initial-crop-height', savedCrop.height!)
  await page.keyboard.press('Escape')
  await expect(cropDialog).toHaveCount(0)
  await expect(heroFrame).toHaveAttribute('data-crop-x', savedCrop.x!)
  await expect(heroFrame).toHaveAttribute('data-crop-y', savedCrop.y!)

  await editorCanvas.getByRole('button', { name: 'Crop / move photograph' }).click()
  await expect(cropDialog).toBeVisible()
  await cropDialog.getByRole('button', { name: 'Cancel', exact: true }).click()
  await expect(cropDialog).toHaveCount(0)
  await expect(heroFrame).toHaveAttribute('data-crop-x', savedCrop.x!)
  await expect(heroFrame).toHaveAttribute('data-crop-y', savedCrop.y!)

  // Restore the initial image state so this acceptance run remains repeatable.
  await inspector.getByRole('button', { name: 'Reset crop' }).click()
  await expect(heroFrame).toHaveAttribute('data-crop', 'legacy')

  // Replace remains a contextual toolbar action, but delegates selection/upload to the proven Payload media picker.
  await editorCanvas.getByRole('button', { name: 'Replace photograph' }).click()
  const mediaHeading = page.getByRole('heading', { name: 'Select Media' })
  await expect(mediaHeading).toBeVisible({ timeout: 5_000 })
  await expect(page.getByRole('button', { name: 'Upload New' })).toBeVisible()
  await mediaHeading.locator('..').locator('button').click()
  await expect(mediaHeading).toHaveCount(0)

  const match = page.url().match(/\/admin\/puck-editor\/pages\/([^/?#]+)/)
  expect(match?.[1]).toBeTruthy()
  const pageId = match![1]

  const readResponse = await page.request.get(`/api/puck/pages/${pageId}`)
  expect(readResponse.ok()).toBeTruthy()
  const readJson = await readResponse.json()
  const originalData = readJson.doc.puckData
  expect(originalData?.content?.length).toBeGreaterThan(0)

  const marker = 'EDITOR LOOP VERIFIED — draft then publish'
  const draftData = structuredClone(originalData)
  const hero = draftData.content.find((item: any) => item.type === 'HeroSection')
  expect(hero).toBeTruthy()
  hero.props.body = marker

  const draftResponse = await page.request.patch(`/api/puck/pages/${pageId}`, {
    data: { puckData: draftData, draft: true },
  })
  expect(draftResponse.ok()).toBeTruthy()

  await page.goto('/')
  await expect(page.getByText(marker)).toHaveCount(0)
  await expect(page.locator('.wc-hero__image img')).toBeVisible()
  await expect(page.locator('.wc-service-card__image')).toHaveCount(6)

  const versionsResponse = await page.request.get(`/api/puck/pages/${pageId}/versions?limit=5`)
  expect(versionsResponse.status()).not.toBe(404)
  expect(versionsResponse.ok()).toBeTruthy()

  const publishResponse = await page.request.patch(`/api/puck/pages/${pageId}`, {
    data: { puckData: draftData, _status: 'published' },
  })
  expect(publishResponse.ok()).toBeTruthy()

  await page.goto('/')
  await expect(page.getByText(marker)).toBeVisible({ timeout: 10_000 })

  const restoreResponse = await page.request.patch(`/api/puck/pages/${pageId}`, {
    data: { puckData: originalData, _status: 'published' },
  })
  expect(restoreResponse.ok()).toBeTruthy()

  await page.goto('/')
  await expect(page.getByText('Clear answers before parts get replaced. Diagnostics, maintenance and major mechanical work for the cars you depend on.')).toBeVisible()

  await page.goto('/editor')
  await expect(page).toHaveURL(/\/admin\/puck-editor\/pages\/.+/, { timeout: 15_000 })
  await expect(page.frameLocator('iframe').first().getByText('Diagnose. Repair. Drive.').first()).toBeVisible({ timeout: 15_000 })
  await page.screenshot({ path: 'test-results/website-creator-editor.png', fullPage: true })
})
