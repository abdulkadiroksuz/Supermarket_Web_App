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

    let shippingCost = parseFloat(document.getElementById("shippingSelect").value);
    total += shippingCost;

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

    if (currentQuantity > 1) {
        quantityElement.innerText = currentQuantity - 1;
        dbUpdateQuantity(productId, currentQuantity - 1);
        updateCart();
    }else{
        removeItem(productId);
    }
}

function increaseQuantity(productId) {
    let product = document.getElementById(productId);
    // Implement your logic to increase the quantity for the specific product
    let quantityElement = product.querySelector(".quantity");
    let currentQuantity = parseInt(quantityElement.innerText);
    if (currentQuantity < 10) {
        quantityElement.innerText = currentQuantity + 1;
        dbUpdateQuantity(productId, currentQuantity + 1);
    }
    updateCart();
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
        data: {
            product_id: productId.substring(1), // remove the 'p' from the id
            new_quantity: newQuantity,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        }
    });
}

// deletion from database
function dbDeleteItem(productId) {
    $.ajax({
        type: "POST",
        url: "delete_cart_item",  // cart app 
        data: {
            product_id: productId.substring(1), // remove the 'p' from the id
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        }
    });
}