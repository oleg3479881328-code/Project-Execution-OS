import 'dotenv/config'
import config from '@payload-config'
import { getPayload } from 'payload'
import { carServiceGarage } from '../sites/car-service-garage'

async function run() {
  const payload = await getPayload({ config })
  const forceSeed = process.env.WC_SEED_FORCE === 'true'

  for (const page of carServiceGarage.pages) {
    const existing = await payload.find({
      collection: 'pages' as any,
      where: { slug: { equals: page.slug } } as any,
      limit: 1,
      draft: true,
      overrideAccess: true,
    })

    const data = {
      ...page,
      _status: 'published',
    } as any

    if (existing.docs[0]) {
      if (forceSeed) {
        await payload.update({
          collection: 'pages' as any,
          id: (existing.docs[0] as any).id,
          data,
          draft: false,
          overrideAccess: true,
        })
      }
    } else {
      await payload.create({
        collection: 'pages' as any,
        data,
        draft: false,
        overrideAccess: true,
      })
    }
  }

  const adminEmail = process.env.WC_ADMIN_EMAIL?.trim()
  const adminPassword = process.env.WC_ADMIN_PASSWORD

  if (adminEmail && adminPassword) {
    const existingAdmin = await payload.find({
      collection: 'users',
      where: { email: { equals: adminEmail } },
      limit: 1,
      overrideAccess: true,
    })

    if (!existingAdmin.docs[0]) {
      await payload.create({
        collection: 'users',
        data: {
          email: adminEmail,
          password: adminPassword,
        },
        overrideAccess: true,
      })
      payload.logger.info(`Created Website Creator admin: ${adminEmail}`)
    }
  }

  payload.logger.info(`Seeded Site Instance: ${carServiceGarage.siteId}${forceSeed ? ' (forced)' : ''}`)
  process.exit(0)
}

run().catch((error) => {
  console.error(error)
  process.exit(1)
})
