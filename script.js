// Smooth scrolling
document.querySelectorAll('nav a').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href'))
      .scrollIntoView({ behavior: 'smooth' });
  });
});

// Highlight active section
window.addEventListener('scroll', () => {
  let sections = document.querySelectorAll('section');
  let scrollPos = window.scrollY + 100;
  sections.forEach(sec => {
    if (sec.offsetTop <= scrollPos && sec.offsetTop + sec.offsetHeight > scrollPos) {
      document.querySelectorAll('nav a').forEach(a => a.classList.remove('active'));
      document.querySelector(`nav a[href="#${sec.id}"]`).classList.add('active');
    }
  });
});
