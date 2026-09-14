import type { SiteInstanceV01 } from '../site-model/types'

const serviceLines = [
  ['Engine diagnostics', 'Warning lights, drivability problems and root-cause troubleshooting before parts are replaced.'],
  ['Brake service', 'Pads, rotors, hubs and related brake-system repair with proper inspection.'],
  ['Suspension & steering', 'Wheel-end, steering and suspension work for predictable handling and safe road manners.'],
  ['Oil change & preventive service', 'Oil, filters and fluid checks as part of a sensible maintenance routine.'],
  ['Electrical systems', 'Starting, charging, wiring and dashboard-system diagnostics.'],
  ['Engine & transmission work', 'Major mechanical jobs and component replacement when diagnosis truly calls for it.'],
]

const content: Array<{ type: string; props: Record<string, unknown> }> = [
  { type: 'Heading', props: { id: 'hero-title', text: 'Diagnose. Repair. Drive.', level: 'h1' } },
  { type: 'Text', props: { id: 'hero-copy', content: 'Clear answers before parts get replaced. Diagnostics, maintenance and major mechanical work for the cars you depend on.' } },
  { type: 'Button', props: { id: 'hero-call', text: 'Call 513-800-6462', link: 'tel:+15138006462' } },
  { type: 'Heading', props: { id: 'services-title', text: 'Explore our services', level: 'h2' } },
  ...serviceLines.flatMap(([name, description], index) => [
    { type: 'Heading', props: { id: `service-${index + 1}-title`, text: name, level: 'h3' } },
    { type: 'Text', props: { id: `service-${index + 1}-copy`, content: description } },
  ]),
  { type: 'Heading', props: { id: 'process-title', text: 'From symptom to solution.', level: 'h2' } },
  { type: 'Text', props: { id: 'process-1', content: '01 — Tell us what the car is doing.' } },
  { type: 'Text', props: { id: 'process-2', content: '02 — We inspect and diagnose.' } },
  { type: 'Text', props: { id: 'process-3', content: '03 — You get a clear next step.' } },
  { type: 'Heading', props: { id: 'cta-title', text: 'When your car needs attention, start here.', level: 'h2' } },
  { type: 'Button', props: { id: 'cta-call', text: 'Call 513-800-6462', link: 'tel:+15138006462' } },
]

export const carServiceGarage: SiteInstanceV01 = {
  schemaVersion: '0.1-draft',
  siteId: 'car-service-garage-ohio',
  business: {
    name: 'Car Service Garage',
    kind: 'auto-repair',
    locationLabel: 'West Chester Township, Ohio',
    contact: {
      phone: '+15138006462',
      phoneDisplay: '513-800-6462',
      address: '9002 Cincinnati Columbus Rd, West Chester Township, OH 45069',
      mapUrl: 'https://maps.app.goo.gl/9JHsFKG121yuTpHt9',
    },
  },
  theme: {
    colors: {
      background: '#0b0d10',
      surface: '#14181d',
      text: '#f5f7f8',
      muted: '#aab3bd',
      accent: '#e53935',
    },
  },
  pages: [
    {
      title: 'Car Service Garage',
      slug: 'home',
      isHomepage: true,
      meta: {
        title: 'Car Service Garage | Auto Repair in West Chester, OH',
        description: 'Independent full-service auto repair in West Chester Township, Ohio. Diagnostics, brakes, suspension, electrical, oil service, engine and transmission repair.',
      },
      puckData: {
        root: { props: {} },
        content,
      },
    },
  ],
}
