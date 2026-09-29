import { expect, test } from '@playwright/test'

test('Car Service Garage renders the light-minimal shared Website Creator landing on desktop and mobile', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 1000 })
  await page.goto('/')

  await expect(page.locator('[data-site-renderer="website-creator-v0.1"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="header"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="hero"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="trust-strip"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="services"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="benefits"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="process"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="reviews-contact"]')).toBeVisible()
  await expect(page.locator('[data-wc-section="footer"]')).toBeVisible()

  await expect(page.getByRole('heading', { name: 'Reliable auto service for your everyday car' })).toBeVisible()
  await expect(page.getByText('Everyday service, handled carefully.')).toBeVisible()
  await expect(page.locator('.wc-service-card')).toHaveCount(4)
  await expect(page.locator('.wc-service-card__image')).toHaveCount(4)
  await expect(page.locator('.wc-process-step')).toHaveCount(4)
  await expect(page.getByRole('link', { name: 'Schedule service' }).first()).toHaveAttribute('href', 'tel:+15138006462')
  await expect(page.locator('body')).not.toHaveCSS('overflow-x', 'scroll')

  await page.screenshot({ path: 'test-results/car-service-garage-desktop.png', fullPage: true })

  await page.setViewportSize({ width: 390, height: 844 })
  await page.reload()
  await expect(page.getByRole('heading', { name: 'Reliable auto service for your everyday car' })).toBeVisible()
  await expect(page.locator('.wc-services__grid')).toBeVisible()
  await expect(page.locator('.wc-service-card')).toHaveCount(4)
  await expect(page.locator('body')).not.toHaveCSS('overflow-x', 'scroll')
  await page.screenshot({ path: 'test-results/car-service-garage-mobile.png', fullPage: true })
})
