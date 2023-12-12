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
    let isFormActive = loginForm.classList.contains('active');
    if (!isFormActive && isClickInsideUserIcon){
        openLoginForm();
    }else if (!(isClickInsideButton || isClickInsideForm || isClickInsideUserIcon)){
        closeLoginForm();
    }else if(isClickInsideUserIcon && isFormActive){
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
}




document.getElementById('showPassword').addEventListener('change', function (e) {
    var passwordInput = document.getElementById('password-input');
    if (e.target.checked) {
      passwordInput.type = 'text';
    } else {
      passwordInput.type = 'password';
    }
  });



