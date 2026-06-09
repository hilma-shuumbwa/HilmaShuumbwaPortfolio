const navToggle = document.querySelector('.nav-toggle');
const navMenu = document.querySelector('#nav-menu');

if (navToggle && navMenu) {
  navToggle.addEventListener('click', () => {
    const isOpen = navMenu.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
  });
}

async function loadJson(path) {
  const response = await fetch(path);
  if (!response.ok) return [];
  return response.json();
}

function renderEvidence(items) {
  const grid = document.querySelector('#evidence-grid');
  if (!grid) return;
  grid.innerHTML = items.map((item) => `
    <article class="evidence-card">
      <img src="${item.image}" alt="${item.title}">
      <div>
        <h3>${item.title}</h3>
        <p>${item.caption}</p>
      </div>
    </article>
  `).join('');
}

function renderCertificates(items) {
  const grid = document.querySelector('#certificate-grid');
  if (!grid) return;
  if (!items.length) {
    grid.innerHTML = '<article class="certificate-card"><h3>Certificate Section</h3><p>Certificate evidence section prepared for showcase review.</p></article>';
    return;
  }
  grid.innerHTML = items.map((item) => `
    <article class="certificate-card">
      <h3>${item.title}</h3>
      <p>Certificate evidence file.</p>
      <a href="${item.file}" target="_blank" rel="noopener">Open certificate</a>
    </article>
  `).join('');
}

loadJson('evidence.json').then(renderEvidence).catch(() => renderEvidence([]));
loadJson('certificates.json').then(renderCertificates).catch(() => renderCertificates([]));
