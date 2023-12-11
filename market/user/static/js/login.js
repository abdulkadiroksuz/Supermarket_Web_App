function openLoginForm() {
    let login = document.getElementById('login-form');
    login.classList.add('active');
}

function closeLoginForm() {
    let login = document.getElementById('login-form');
    login.classList.remove('active');
}

// Function to submit the login form
function submitLoginForm() {
    document.getElementById('login-form').submit();
}

// Event listener for the login button click
document.getElementById('login-button').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent the default form submission
    submitLoginForm(); // Manually submit the form
});

// Event listener for the Enter key press in the login form
document.getElementById('login-form').addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default form submission
        submitLoginForm(); // Manually submit the form
    }
});

document.addEventListener('click', function (event) {
    let loginForm = document.getElementById('login-form');
    let loginButton = document.getElementById('login-button');
    let userIcon = document.getElementById('user-icon');

    // Check if the click is outside the form and button
    let isClickInsideForm = loginForm.contains(event.target);
    let isClickInsideButton = loginButton.contains(event.target);
    let isClickInsideUserIcon = userIcon.contains(event.target);
    if (!(isClickInsideForm || isClickInsideButton || isClickInsideUserIcon)) {
        closeLoginForm();
    }
});

window.onscroll = () => {
    closeLoginForm();
}

function saveCredentials() {
    let usernameInput = document.querySelector('input[name="username"]');
    let passwordInput = document.querySelector('input[name="password"]');
    let rememberCheckbox = document.getElementById('remember-me');
    if (rememberCheckbox.checked) {
        // If the "Remember me" checkbox is checked, save the credentials in cookies
        document.cookie = `savedUsername=${encodeURIComponent(usernameInput.value)};`;
        document.cookie = `savedPassword=${encodeURIComponent(passwordInput.value)};`;
    } else {
        // If not checked, clear any saved credentials by setting expiration in the past
        document.cookie = 'savedUsername=; expires=Thu, 01 Jan 1970 00:00:00 UTC;';
        document.cookie = 'savedPassword=; expires=Thu, 01 Jan 1970 00:00:00 UTC;';
    }
}

// Function to get the value of a cookie by its name
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);

    if (parts.length === 2) {
        return parts.pop().split(';').shift();
    }
}

function loadCredentials() {
    let savedUsername = getCookie('savedUsername');
    let savedPassword = getCookie('savedPassword');

    let usernameInput = document.querySelector('input[name="username"]');
    let passwordInput = document.querySelector('input[name="password"]');
    let rememberCheckbox = document.getElementById('remember-me');

    if (savedUsername && savedPassword) {
        // If the saved credentials are valid, fill in the form fields
        usernameInput.value = decodeURIComponent(savedUsername);
        passwordInput.value = decodeURIComponent(savedPassword);
        rememberCheckbox.checked = true;
    }
}

window.onload = function () {
    loadCredentials();
    updateNavbarCart();
}

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




