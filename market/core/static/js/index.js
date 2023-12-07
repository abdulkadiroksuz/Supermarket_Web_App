document.addEventListener("DOMContentLoaded", function() {
    var homeBanner = document.getElementById("home-banner");

    function handleScroll() {
        var scrollY = window.scrollY || window.pageYOffset;
        var scrollThreshold = 250; // Adjust this value based on when you want the effect to start

        if (scrollY > scrollThreshold) {
            homeBanner.classList.add("banner-hidden");
        } else {
            homeBanner.classList.remove("banner-hidden");
        }
    }

    window.addEventListener("scroll", handleScroll);
});


let login = document.querySelector('.login-form');

document.querySelector('#user-icon').onclick = () =>{
  login.classList.toggle('active');
}

window.onscroll = () =>{
  login.classList.remove('active');
}

// var swiper = new Swiper(".review-slider", {
//   spaceBetween:20,
//   centeredSlides: true,
//   autoplay: {
//     delay: 7500,
//     disableOnInteraction: false,
//   },
//   loop: true,
//   breakpoints: {
//     0:{
//       slidesPerView: 1,
//     },
//     768:{
//       slidesPerView: 2,
//     },
//     991:{
//       slidesPerView: 3,
//     },
//   },
// });