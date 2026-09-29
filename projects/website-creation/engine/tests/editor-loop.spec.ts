import { expect, test } from '@playwright/test'

test('CSG Puck editor uses GitHub-backed draft, media, publish, and reload state', async ({ page }) => {
  const username = process.env.CSG_EDITOR_USERNAME || 'editor'
  const password = process.env.CSG_EDITOR_PASSWORD
  expect(password, 'CSG_EDITOR_PASSWORD must be set for editor E2E').toBeTruthy()

  await page.goto('/editor')
  await expect(page).toHaveURL(/\/editor\/login/)
  await page.getByLabel('Username').fill(username)
  await page.getByLabel('Password').fill(password!)
  await page.getByRole('button', { name: 'Open editor' }).click()
  await expect(page).toHaveURL(/\/editor$/)
  await expect(page.getByRole('button', { name: 'Save draft' })).toBeVisible()
  await expect(page.getByRole('button', { name: 'Publish' }).first()).toBeVisible()

  const editorCanvas = page.frameLocator('iframe').first()
  await expect(editorCanvas.getByText('Reliable auto service for your everyday car').first()).toBeVisible({ timeout: 15_000 })
  await expect(editorCanvas.locator('.wc-service-card__image')).toHaveCount(4)

  const heroFrame = editorCanvas.locator('.wc-editable-image--hero .wc-image-frame').first()
  await heroFrame.click({ position: { x: 80, y: 80 } })
  await expect(editorCanvas.getByRole('toolbar', { name: 'Image controls' })).toBeVisible()
  await expect(editorCanvas.getByRole('button', { name: 'Replace photograph' })).toBeVisible()
  await expect(editorCanvas.getByRole('button', { name: /Crop \/ move photograph/ })).toBeVisible()

  const inspector = page.locator('[data-wc-image-inspector="hero"]')
  await expect(inspector).toBeVisible()
  const shape = inspector.locator('select').first()
  await shape.selectOption('square')
  await expect(heroFrame).toHaveAttribute('data-ratio', 'square')
  await shape.selectOption('landscape')
  await expect(heroFrame).toHaveAttribute('data-ratio', 'landscape')
  const zoom = inspector.locator('input[type="range"]').first()
  await zoom.fill('1.25')
  await expect(inspector.getByText('Zoom · 1.25×')).toBeVisible()

  await editorCanvas.getByRole('button', { name: 'Replace photograph' }).click()
  await expect(page.getByRole('heading', { name: 'Select Media' })).toBeVisible({ timeout: 5_000 })
  await expect(page.getByRole('button', { name: 'Upload New' })).toBeVisible()
  await page.keyboard.press('Escape')

  const upload = await page.evaluate(async () => {
    const binary = Uint8Array.from(atob('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII='), (character) => character.charCodeAt(0))
    const form = new FormData()
    form.append('file', new File([binary], 'csg-upload.png', { type: 'image/png' }))
    form.append('alt', 'Git-backed uploaded CSG image')
    const response = await fetch('/api/csg/media', { method: 'POST', body: form })
    return { ok: response.ok, body: await response.json() }
  })
  expect(upload.ok).toBeTruthy()
  expect(upload.body.doc.url).toMatch(/^\/uploads\/csg\/.+/)

  const stateResponse = await page.evaluate(async () => {
    const response = await fetch('/api/csg/state?scope=published')
    return { ok: response.ok, body: await response.json() }
  })
  expect(stateResponse.ok).toBeTruthy()
  const published = stateResponse.body as { state: any }
  const draft = structuredClone(published.state)
  const hero = draft.pages[0].puckData.content.find((item: any) => item.type === 'HeroSection')
  expect(hero).toBeTruthy()
  const marker = `GITHUB BACKED CSG ROUND TRIP ${Date.now()}`
  hero.props.body = marker

  const draftResponse = await page.evaluate(async (state) => {
    const response = await fetch('/api/csg/draft', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ state }) })
    return { ok: response.ok, body: await response.json() }
  }, draft)
  expect(draftResponse.ok).toBeTruthy()
  await page.getByRole('button', { name: 'Save draft' }).click({ force: true })

  await page.goto('/')
  await expect(page.getByText(marker)).toHaveCount(0)

  const publishResponse = await page.evaluate(async () => {
    const response = await fetch('/api/csg/publish', { method: 'POST' })
    return { ok: response.ok, body: await response.json() }
  })
  expect(publishResponse.ok).toBeTruthy()
  await page.goto('/')
  await expect(page.getByText(marker)).toBeVisible()

  await page.goto('/editor')
  await expect(editorCanvas.getByText(marker).first()).toBeVisible({ timeout: 15_000 })
  const health = await page.evaluate(async () => (await fetch('/health')).json())
  expect(health).toMatchObject({ persistence: 'github', database: 'not-required' })
})
