function updateCart() {
    var total = 0.0;
    var products = document.querySelectorAll(".product")
    var productsQuantity = products.length;

    for (var i = 0; i < productsQuantity; i++) {
        let product = products[i];
        let price = parseFloat(product.querySelector(".product-price").innerText.replace("$", ""));
        let quantity = parseInt(product.querySelector(".quantity").innerText);
        total += (price * quantity);
    }

    document.getElementsByClassName("col align-self-center text-right text-muted")[0].innerHTML = productsQuantity + " products";
    document.getElementsByClassName("tot-items")[0].innerHTML = productsQuantity + " ITEMS";
    document.querySelectorAll(".tot-price").forEach(function(element) {
        element.innerText = "$" + total.toFixed(2);
    });
}


function decreaseQuantity(productId) {
    let product = document.getElementById(productId);
    // Implement your logic to decrease the quantity for the specific product
    let quantityElement = product.querySelector(".quantity");
    let currentQuantity = parseInt(quantityElement.innerText);
    let newQuantity = currentQuantity - 1;
    if (currentQuantity > 1) {
        dbUpdateQuantity(productId, newQuantity);
    }else{
        removeItem(productId);
    }
}

function increaseQuantity(productId) {
    let product = document.getElementById(productId);
    // Implement your logic to increase the quantity for the specific product
    let quantityElement = product.querySelector(".quantity");
    let currentQuantity = parseInt(quantityElement.innerText);
    let new_quantity = currentQuantity + 1;
    if (new_quantity <= 10) {
        dbUpdateQuantity(productId, new_quantity);
    }else{
        showErrorModal("You can't add more than 10 items for each product");
    }
}

function removeItem(productId) {
    let product = document.getElementById(productId);
    product.remove();
    dbDeleteItem(productId);
    updateCart();
}

// update quantity in database
function dbUpdateQuantity(productId, newQuantity) {
    $.ajax({
        type: "POST",
        url: "update_cart_item",  // cart app 
        headers: {
            'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        data: {
            product_id: productId.substring(1), // remove the 'p' from the id
            new_quantity: newQuantity,
        },
        success: function (response) {
            let product = document.getElementById(productId);
            let quantityElement = product.querySelector(".quantity");
            if (response.success) {
                quantityElement.innerText = newQuantity
            }else{
                let stock = response.stock;
                if(stock !== -1){
                    quantityElement.innerText = response.stock;
                }
                showErrorModal(response.error);
            }
            updateCart();
        },
        error: function (response) {
            console.log(response);
        },
    });
}

// deletion from database
function dbDeleteItem(productId) {
    $.ajax({
        type: "POST",
        url: "delete_cart_item",  // cart app 
        headers: {
            'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        data: {
            product_id: productId.substring(1), // remove the 'p' from the id
        },
        success: function (response) {
            if (response.success) {
                updateNavbarCart();
            }
        },
    });
}