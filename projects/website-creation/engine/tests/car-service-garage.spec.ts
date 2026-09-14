import { expect, test } from '@playwright/test'

test('Car Service Garage Site Instance renders the canonical content', async ({ page }) => {
  await page.setViewportSize({ width: 1440, height: 1000 })
  await page.goto('/')
  await expect(page.locator('[data-site-renderer="website-creator-v0.1"]')).toBeVisible()
  await expect(page.getByText('Diagnose. Repair. Drive.')).toBeVisible()
  await expect(page.getByText('Explore our services')).toBeVisible()
  await expect(page.getByRole('link', { name: 'Call 513-800-6462' }).first()).toHaveAttribute('href', 'tel:+15138006462')
  await page.screenshot({ path: 'test-results/car-service-garage-desktop.png', fullPage: true })

  await page.setViewportSize({ width: 390, height: 844 })
  await page.reload()
  await expect(page.getByText('Diagnose. Repair. Drive.')).toBeVisible()
  await page.screenshot({ path: 'test-results/car-service-garage-mobile.png', fullPage: true })
})
