import 'dotenv/config'
import config from '@payload-config'
import { getPayload } from 'payload'
import { carServiceGarage } from '../sites/car-service-garage'

async function run() {
  const payload = await getPayload({ config })

  for (const page of carServiceGarage.pages) {
    const existing = await payload.find({
      collection: 'pages' as any,
      where: { slug: { equals: page.slug } } as any,
      limit: 1,
    })

    const data = {
      ...page,
      _status: 'published',
    } as any

    if (existing.docs[0]) {
      await payload.update({
        collection: 'pages' as any,
        id: (existing.docs[0] as any).id,
        data,
        draft: false,
      })
    } else {
      await payload.create({
        collection: 'pages' as any,
        data,
        draft: false,
      })
    }
  }

  payload.logger.info(`Seeded Site Instance: ${carServiceGarage.siteId}`)
  process.exit(0)
}

run().catch((error) => {
  console.error(error)
  process.exit(1)
})
