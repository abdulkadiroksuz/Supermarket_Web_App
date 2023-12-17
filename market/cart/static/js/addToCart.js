function dbAddToCart(product_slug, updateUrl) {
    try {        
        var element = document.getElementById(product_slug);
        var quantityInput = element.querySelector('.quantity input');
        var quantity = parseInt(quantityInput.value);
    } catch (error) {
        var quantity = 1;
    }
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
                try {
                    quantityInput.value = 1;
                } catch (error) {
                    console.log('.quantity input not found');
                }
            } else {
                showErrorModal(response.error);
            }
        },
        error: function (response) {
            console.log(response);
        },
    });
}

function goBack() {
    window.history.back();
}