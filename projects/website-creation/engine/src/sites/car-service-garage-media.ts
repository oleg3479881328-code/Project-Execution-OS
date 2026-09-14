import type { MediaReference } from '../puck/image-editor/types'

const seed = (id: string, filename: string, alt: string): MediaReference => ({
  id: `seed-csg-${id}`,
  url: `/seed/car-service-garage/${filename}`,
  alt,
})

export const carServiceGarageMedia = {
  hero: seed('hero', 'hero.webp', 'Mechanic servicing a black BMW inside Car Service Garage'),
  diagnostics: seed('diagnostics', 'diagnostics.webp', 'Technician using diagnostic equipment on an engine'),
  brakes: seed('brakes', 'brakes.webp', 'Brake rotor and wheel hub during brake service'),
  suspension: seed('suspension', 'suspension.webp', 'Mechanic inspecting suspension and wheel-well components'),
  oil: seed('oil', 'oil.webp', 'Under-hood maintenance and preventive service'),
  electrical: seed('electrical', 'electrical.webp', 'Technician diagnosing dashboard and electrical systems'),
  major: seed('major', 'major.webp', 'Major engine repair with powertrain removed from the vehicle'),
} as const
