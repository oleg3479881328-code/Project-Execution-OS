import type { SiteInstanceV01 } from '../site-model/types'

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
        content: [
          {
            type: 'HeroSection',
            props: {
              id: 'hero',
              eyebrow: 'Independent auto repair · West Chester, Ohio',
              title: 'Diagnose. Repair. Drive.',
              highlight: 'Drive.',
              body: 'Clear answers before parts get replaced. Diagnostics, maintenance and major mechanical work for the cars you depend on.',
              primaryLabel: 'Call 513-800-6462',
              primaryHref: 'tel:+15138006462',
              secondaryLabel: 'Explore services',
              secondaryHref: '#services',
              imageUrl: '',
              imageAlt: 'Professional auto repair garage',
            },
          },
          {
            type: 'ServicesSection',
            props: {
              id: 'services',
              eyebrow: 'Built around the problem',
              heading: 'Explore our services',
              intro: 'Each service starts with the same principle: understand the cause before replacing parts.',
              services: [
                { kicker: '01 · DIAGNOSTICS', title: 'Engine diagnostics', body: 'Warning lights, drivability problems and root-cause troubleshooting before parts are replaced.', actionLabel: 'Schedule service', actionHref: 'tel:+15138006462' },
                { kicker: '02 · BRAKES', title: 'Brake service', body: 'Pads, rotors, hubs and related brake-system repair with proper inspection.', actionLabel: 'Schedule service', actionHref: 'tel:+15138006462' },
                { kicker: '03 · CHASSIS', title: 'Suspension & steering', body: 'Wheel-end, steering and suspension work for predictable handling and safe road manners.', actionLabel: 'Schedule service', actionHref: 'tel:+15138006462' },
                { kicker: '04 · MAINTENANCE', title: 'Oil change & preventive service', body: 'Oil, filters and fluid checks as part of a sensible maintenance routine.', actionLabel: 'Schedule service', actionHref: 'tel:+15138006462' },
                { kicker: '05 · ELECTRICAL', title: 'Electrical systems', body: 'Starting, charging, wiring and dashboard-system diagnostics.', actionLabel: 'Schedule service', actionHref: 'tel:+15138006462' },
                { kicker: '06 · MAJOR REPAIR', title: 'Engine & transmission work', body: 'Major mechanical jobs and component replacement when diagnosis truly calls for it.', actionLabel: 'Schedule service', actionHref: 'tel:+15138006462' },
              ],
            },
          },
          {
            type: 'ProcessSection',
            props: {
              id: 'process',
              eyebrow: 'A simple process',
              heading: 'From symptom to solution.',
              steps: [
                { number: '01', title: 'Tell us what the car is doing.', body: 'Call or message with the symptom, warning light or repair concern.' },
                { number: '02', title: 'We inspect and diagnose.', body: 'The goal is to verify the cause before committing you to parts and labor.' },
                { number: '03', title: 'You get a clear next step.', body: 'Repair what matters now and make the decision with better information.' },
              ],
            },
          },
          {
            type: 'CtaSection',
            props: {
              id: 'cta',
              eyebrow: 'West Chester Township, Ohio',
              heading: 'When your car needs attention, start here.',
              body: 'Call or message before you arrive so the shop can plan the right next step for your vehicle.',
              primaryLabel: 'Call 513-800-6462',
              primaryHref: 'tel:+15138006462',
              secondaryLabel: 'Get directions',
              secondaryHref: 'https://maps.app.goo.gl/9JHsFKG121yuTpHt9',
            },
          },
          {
            type: 'FooterSection',
            props: {
              id: 'footer',
              brand: 'CAR SERVICE GARAGE',
              address: '9002 Cincinnati Columbus Rd\nWest Chester Township, OH 45069',
              phoneLabel: '513-800-6462',
              phoneHref: 'tel:+15138006462',
              tagline: 'Independent auto repair in West Chester Township',
            },
          },
        ],
      },
    },
  ],
}
