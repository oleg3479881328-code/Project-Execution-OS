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

  // Use the visible inspector control to prove the official Puck setData bridge persists a real user edit.
  const shape = inspector.locator('select').first()
  await expect(shape).toBeVisible()
  await shape.selectOption('square')
  await expect(heroFrame).toHaveAttribute('data-ratio', 'square')
  await shape.selectOption('portrait')
  await expect(heroFrame).toHaveAttribute('data-ratio', 'portrait')

  // Replace remains a contextual toolbar action, but delegates selection/upload to the proven Payload media picker.
  await editorCanvas.getByRole('button', { name: 'Replace photograph' }).click()
  await expect(page.getByRole('heading', { name: 'Select Media' })).toBeVisible({ timeout: 5_000 })
  await expect(page.getByRole('button', { name: 'Upload New' })).toBeVisible()
  await page.keyboard.press('Escape')
  await expect(page.getByRole('heading', { name: 'Select Media' })).toHaveCount(0)

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
