function openLoginForm() {
    let login = document.getElementById('login-form');
    login.classList.add('active');
}

function closeLoginForm() {
    let login = document.getElementById('login-form');
    login.classList.remove('active');
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


document.getElementById('login-button').addEventListener('click', function(event) {
    event.preventDefault(); // Prevent the default form submission
    document.getElementById('login-form').submit(); // Manually submit the form
});

window.onload = function () {
    loadCredentials();
}

window.onscroll = () => {
    closeLoginForm();
}