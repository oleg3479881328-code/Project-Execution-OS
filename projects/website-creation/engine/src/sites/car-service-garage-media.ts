import type { MediaReference } from '../puck/image-editor/types'

// Deterministic seed fixtures belong to Website Creator itself so clean CI,
// local development, and staging do not depend on an unrelated demo host.
// Real owner-selected photographs continue to use Payload's Media collection.
const seedMediaBase = '/seed-media'

const seed = (id: string, filename: string, alt: string): MediaReference => ({
  id: `seed-csg-${id}`,
  url: `${seedMediaBase}/${filename}`,
  alt,
})

export const carServiceGarageMedia = {
  hero: seed('hero', 'hero.svg', 'Mechanic servicing a black BMW inside Car Service Garage'),
  diagnostics: seed('diagnostics', 'diagnostics.svg', 'Technician using diagnostic equipment on an engine'),
  brakes: seed('brakes', 'brakes.svg', 'Brake rotor and wheel hub during brake service'),
  suspension: seed('suspension', 'suspension.svg', 'Mechanic inspecting suspension and wheel-well components'),
  oil: seed('oil', 'oil.svg', 'Under-hood maintenance and preventive service'),
  electrical: seed('electrical', 'electrical.svg', 'Technician diagnosing dashboard and electrical systems'),
  major: seed('major', 'major.svg', 'Major engine repair with powertrain removed from the vehicle'),
} as const
