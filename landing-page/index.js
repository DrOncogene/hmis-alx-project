const openBtn = document.querySelector(".menu-open");
const closeBtn = document.querySelector(".menu-close");
const mobileMenu = document.querySelector(".responsive-menu");

openBtn.addEventListener('click', (e)=>{
  e.preventDefault();
  openBtn.classList.toggle('hidden');
  closeBtn.classList.toggle('hidden');
  mobileMenu.classList.toggle('show');
});

openBtn.addEventListener('click', (e)=>{
  e.preventDefault();
  closeBtn.classList.toggle('hidden');
  openBtn.classList.toggle('hidden');
  mobileMenu.classList.toggle('show');
});