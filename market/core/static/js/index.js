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
