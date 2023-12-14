function dbAddToCart(product_slug, updateUrl) {
    var element = document.getElementById(product_slug);
    var quantityInput = element.querySelector('.quantity input');
    var quantity = parseInt(quantityInput.value);
    $.ajax({
        type: 'POST',
        url: updateUrl,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        data: {
            'product_slug': product_slug,
            'quantity': quantity,
        },
        success: function () {
            updateNavbarCart();
            quantityInput.value = 1;
        },
    });
}