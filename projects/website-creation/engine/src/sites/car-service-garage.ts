import type { SiteInstanceV01 } from '../site-model/types'
import { carServiceGarageMedia as media } from './car-service-garage-media'

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
        title: 'Car Service Garage | Tires, Electrical, Oil & Detailing in West Chester, OH',
        description: 'Independent auto service in West Chester Township, Ohio. Tire mounting and balancing, auto electrical diagnostics and repair, oil changes, and interior detailing.',
      },
      puckData: {
        root: { props: {} },
        content: [
          {
            type: 'HeroSection',
            props: {
              id: 'hero',
              eyebrow: 'Tires · Electrical · Oil · Interior detailing · West Chester, Ohio',
              title: 'Four essential services. One reliable shop.',
              highlight: 'One reliable shop.',
              body: 'Straightforward automotive service for the jobs drivers need most: tire mounting and balancing, electrical diagnostics, oil changes, and a cleaner interior.',
              primaryLabel: 'Call 513-800-6462',
              primaryHref: 'tel:+15138006462',
              secondaryLabel: 'Explore services',
              secondaryHref: '#services',
              image: media.hero,
              imageAlt: media.hero.alt,
              imageCredit: '',
              imageRatio: 'portrait',
              imageFitMode: 'fill',
              imageZoom: 1,
              imageFocalX: 55,
              imageFocalY: 50,
            },
          },
          {
            type: 'ServicesSection',
            props: {
              id: 'services',
              eyebrow: 'What we do',
              heading: 'Four services. Done right.',
              intro: 'Focused service, clear communication, and practical work for the vehicle you drive every day.',
              services: [
                {
                  kicker: '01 · TIRES',
                  title: 'Tire service & mounting',
                  body: 'Tire mounting, balancing, rotations and seasonal tire swaps for a smoother, safer drive.',
                  actionLabel: 'Schedule tire service',
                  actionHref: 'tel:+15138006462',
                  image: media.suspension,
                  imageAlt: 'Wheel and suspension area during tire and wheel service',
                },
                {
                  kicker: '02 · ELECTRICAL',
                  title: 'Auto electrical',
                  body: 'Diagnostics and repair for batteries, starting and charging systems, wiring, lights and dashboard electrical issues.',
                  actionLabel: 'Schedule electrical service',
                  actionHref: 'tel:+15138006462',
                  image: media.electrical,
                  imageAlt: media.electrical.alt,
                },
                {
                  kicker: '03 · OIL SERVICE',
                  title: 'Oil change',
                  body: 'Engine oil and filter service with basic under-hood checks to help keep routine maintenance simple.',
                  actionLabel: 'Schedule an oil change',
                  actionHref: 'tel:+15138006462',
                  image: media.oil,
                  imageAlt: media.oil.alt,
                },
                {
                  kicker: '04 · DETAILING',
                  title: 'Interior detailing',
                  body: 'Interior cleaning and refresh for seats, carpets, trim and high-touch surfaces so the cabin feels clean again.',
                  actionLabel: 'Schedule detailing',
                  actionHref: 'tel:+15138006462',
                  image: null,
                  imageAlt: '',
                },
              ],
            },
          },
          {
            type: 'ProcessSection',
            props: {
              id: 'process',
              eyebrow: 'Simple from the start',
              heading: 'Book. Service. Drive away.',
              steps: [
                { number: '01', title: 'Tell us what you need.', body: 'Call with the service you need and the vehicle you are bringing in.' },
                { number: '02', title: 'We inspect before we work.', body: 'We confirm the condition and the service scope before moving ahead.' },
                { number: '03', title: 'Get the job done clearly.', body: 'You get straightforward service and a clear next step before you leave.' },
              ],
            },
          },
          {
            type: 'CtaSection',
            props: {
              id: 'cta',
              eyebrow: 'West Chester Township, Ohio',
              heading: 'Need tires, electrical work, an oil change or a cleaner interior?',
              body: 'Call before you arrive and we will help plan the right service for your vehicle.',
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
              tagline: 'Tires · Electrical · Oil · Interior detailing',
            },
          },
        ],
      },
    },
  ],
}
