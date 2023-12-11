function dbAddToCart(product_slug, updateUrl) {
    var element = document.getElementById(product_slug);
    var quantityInput = element.querySelector('.quantity input');
    var quantity = parseInt(quantityInput.value);

    $.ajax({
        type: 'POST',
        url: updateUrl,
        data: {
            'product_slug': product_slug,
            'quantity': quantity,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function () {
            updateNavbarCart();
            quantityInput.value = 1;
        }
    });
}