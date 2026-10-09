/* Optional enhancement: every entry and source is already present in HTML. */
(() => {
  const form = document.getElementById('timeline-filters');
  if (!form) return;
  const query = document.getElementById('timeline-query');
  const series = document.getElementById('timeline-series');
  const entries = [...document.querySelectorAll('.wc-event')];
  const texts = entries.map(entry => entry.textContent.toLocaleLowerCase());
  const count = document.getElementById('timeline-count');
  const filter = () => {
    const words = query.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    entries.forEach((entry, index) => {
      const match = (!series.value || entry.dataset.series === series.value) && words.every(word => texts[index].includes(word));
      entry.hidden = !match;
      visible += Number(match);
    });
    count.textContent = `${visible} of ${entries.length} entries shown`;
    document.getElementById('timeline-empty').hidden = visible !== 0;
  };
  const revealHash = () => {
    const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
    if (!target) return;
    const entry = target.closest('.wc-event');
    if (entry?.hidden) { form.reset(); query.value = ''; series.value = ''; filter(); }
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === 'DETAILS') parent.open = true;
    }
    target.scrollIntoView();
  };
  form.hidden = false;
  form.addEventListener('submit', event => event.preventDefault());
  query.addEventListener('input', filter);
  series.addEventListener('change', filter);
  form.addEventListener('reset', () => { query.value = ''; series.value = ''; filter(); });
  window.addEventListener('hashchange', revealHash);
  filter(); revealHash();
  const today = new Date();
  const todayString = `${today.getFullYear()}-${String(today.getMonth()+1).padStart(2,'0')}-${String(today.getDate()).padStart(2,'0')}`;
  document.querySelectorAll('.wc-fresh[data-due]').forEach(element => {
    if (element.dataset.due && todayString > element.dataset.due) {
      element.append(' Review overdue by this device’s date; no newer successful check is recorded.');
      element.classList.add('wc-overdue');
    }
  });
})();
