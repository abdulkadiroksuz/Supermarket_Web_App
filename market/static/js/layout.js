// gets number of items in cart in database
function updateNavbarCart() {
    var updateUrl = document.getElementById('cart-icon').getAttribute('data-update-url');
    $.ajax({
        type: "GET",
        url: updateUrl,
        success: function (data) {
            var cartCountSpan = document.querySelector('#cart-icon span');
            var cartCount = parseInt(data.total_cart_products);

            cartCountSpan.innerText = cartCount;
        },
    });
}

window.onload = function () {
    updateNavbarCart();
}