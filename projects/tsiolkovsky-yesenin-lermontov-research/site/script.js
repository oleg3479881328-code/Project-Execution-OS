const links = [...document.querySelectorAll('nav a[href^="#"]')];
const sections = links.map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean);

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    links.forEach(a => a.removeAttribute('aria-current'));
    const active = links.find(a => a.getAttribute('href') === `#${entry.target.id}`);
    if (active) active.setAttribute('aria-current', 'page');
  });
}, { rootMargin: '-35% 0px -55% 0px', threshold: 0 });

sections.forEach(section => observer.observe(section));

// Inline evidence links: every substantive research claim gets a nearby,
// human-readable clickable label instead of exposing a raw URL.
const SOURCES = {
  tsiolkovskyStudy: 'https://www.tsiolkovsky.org/ru/kosmicheskaya-filosofiya/%D0%B8%D0%B7%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B0%D0%B2%D1%82%D0%BE%D0%B1%D0%B8%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B9-%D1%86%D0%B8%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B3%D0%BE/',
  fatum: 'https://www.tsiolkovsky.org/ru/kosmicheskaya-filosofiya/%D1%84%D0%B0%D1%82%D1%83%D0%BC-%D1%81%D1%83%D0%B4%D1%8C%D0%B1%D0%B0-%D1%80%D0%BE%D0%BA-%D1%86%D0%B8%D0%BE%D0%BB%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9/',
  gmik: 'https://gmik.ru/2017/09/27/tsiolkovskiy-i-gorkiy/',
  imli: 'https://imli.ru/arkhivnye-i-muzejnye-podrazdeleniya/arkhiv-a-m-gorkogo',
  yeseninFeb: 'https://feb-web.ru/feb/esenin/texts/e72/e72-1612.htm?cmd=p',
  yeseninRsl: 'https://search.rsl.ru/ru/record/01009060387',
  lermontovDemon: 'https://www.litfund.ru/auction/438/188/',
  lermontovPoems: 'https://search.rsl.ru/ru/record/01009114658',
  lermontovWorldcat: 'https://search.worldcat.org/title/Polnoe-sobranie-sochinenij/oclc/6214645'
};

function addSource(el, url) {
  if (!el || el.querySelector(':scope > .inline-source')) return;
  const a = document.createElement('a');
  a.className = 'inline-source';
  a.href = url;
  a.target = '_blank';
  a.rel = 'noreferrer';
  a.textContent = 'Источник';
  a.setAttribute('aria-label', 'Открыть источник для этого утверждения');
  el.appendChild(a);
}

// Key findings cards.
const findingCards = document.querySelectorAll('#findings .card');
addSource(findingCards[0], SOURCES.tsiolkovskyStudy);
addSource(findingCards[1], SOURCES.yeseninFeb);
addSource(findingCards[2], SOURCES.lermontovPoems);

// Tsiolkovsky section: thesis-level evidence.
const tsiolkovskyLead = document.querySelector('#tsiolkovsky .lead-small');
addSource(tsiolkovskyLead, SOURCES.tsiolkovskyStudy);
const evidence = document.querySelectorAll('#tsiolkovsky .evidence');
addSource(evidence[0], SOURCES.tsiolkovskyStudy);
addSource(evidence[1], SOURCES.tsiolkovskyStudy);
addSource(evidence[2], SOURCES.imli);
addSource(evidence[3], SOURCES.tsiolkovskyStudy);

// Timeline claims.
const timelineItems = document.querySelectorAll('#tsiolkovsky .timeline li');
addSource(timelineItems[0]?.querySelector('div'), SOURCES.fatum);
addSource(timelineItems[1]?.querySelector('div'), SOURCES.tsiolkovskyStudy);
addSource(timelineItems[2]?.querySelector('div'), SOURCES.tsiolkovskyStudy);
addSource(timelineItems[3]?.querySelector('div'), SOURCES.tsiolkovskyStudy);

// Archive orientations.
const archiveClaims = document.querySelectorAll('#tsiolkovsky .archive-list p');
addSource(archiveClaims[0], SOURCES.tsiolkovskyStudy);
addSource(archiveClaims[1], SOURCES.gmik);
addSource(archiveClaims[2], SOURCES.imli);

// Yesenin claims and bibliographic card.
addSource(document.querySelector('#yesenin .book-card'), SOURCES.yeseninRsl);
const yeseninClaims = document.querySelectorAll('#yesenin .prose p');
addSource(yeseninClaims[0], SOURCES.yeseninFeb);
addSource(yeseninClaims[1], SOURCES.yeseninRsl);

// Lermontov candidate rows: attach the strongest direct catalogue/example source available.
const lermontovRows = document.querySelectorAll('#lermontov tbody tr');
addSource(lermontovRows[0]?.querySelector('td:first-child'), SOURCES.lermontovWorldcat);
addSource(lermontovRows[1]?.querySelector('td:first-child'), SOURCES.lermontovPoems);
addSource(lermontovRows[2]?.querySelector('td:first-child'), SOURCES.lermontovDemon);
addSource(lermontovRows[3]?.querySelector('td:first-child'), SOURCES.lermontovPoems);
addSource(lermontovRows[4]?.querySelector('td:first-child'), SOURCES.lermontovWorldcat);

// Cross-check statements.
const checks = document.querySelectorAll('#disputed .check');
addSource(checks[0]?.querySelector('div'), SOURCES.tsiolkovskyStudy);
addSource(checks[1]?.querySelector('div'), SOURCES.imli);
addSource(checks[2]?.querySelector('div'), SOURCES.tsiolkovskyStudy);
addSource(checks[3]?.querySelector('div'), SOURCES.lermontovDemon);

// Style is injected here so the feature remains self-contained and deploy-safe.
const sourceStyle = document.createElement('style');
sourceStyle.textContent = `
.inline-source{display:inline-block;margin:10px 0 0 10px;font-family:var(--sans);font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--accent);text-decoration:none;border-bottom:1px solid currentColor;line-height:1.35}
.inline-source:hover{opacity:.65}
.card>.inline-source,.evidence>.inline-source,.book-card>.inline-source{margin-left:0}
.sources .inline-source{color:#d98978}
`;
document.head.appendChild(sourceStyle);
