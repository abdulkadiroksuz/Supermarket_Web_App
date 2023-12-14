function dbAddToCart(product_slug, updateUrl) {
    var element = document.getElementById(product_slug);
    var quantityInput = element.querySelector('.quantity input');
    var quantity = parseInt(quantityInput.value);
    $.ajax({
        type: 'POST',
        url: updateUrl,
        headers: {
            'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        data: {
            'product_slug': product_slug,
            'quantity': quantity,
        },
        success: function (response) {
            if (response.success) {
                updateNavbarCart();
                quantityInput.value = 1;
            } else {
                showErrorModal(response.error);
            }
        },
        error: function (response) {
            console.log(response);
        },
    });
}