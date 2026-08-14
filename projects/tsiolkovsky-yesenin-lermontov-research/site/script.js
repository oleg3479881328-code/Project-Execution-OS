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
