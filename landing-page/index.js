const menuBtn = document.querySelector(".menu-btn");
const mobileMenu = document.querySelector(".responsive-menu");
const bodyBlur = document.querySelector(".body-blur")
const body = document.body

menuBtn.addEventListener('click', (e)=>{
  menuBtn.classList.toggle('btn-open');
  mobileMenu.classList.toggle('show');
  bodyBlur.classList.toggle('show-blur')
  body.classList.toggle('noscroll')
});
