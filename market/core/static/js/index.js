document.addEventListener("DOMContentLoaded", function() {
    var homeBanner = document.getElementById("home-banner");

    function handleScroll() {
        var scrollY = window.scrollY || window.pageYOffset;
        var scrollThreshold = 250; // Adjust this value based on when you want the effect to start

        if (scrollY > scrollThreshold) {
            homeBanner.classList.add("banner-hidden");
        } else {
            homeBanner.classList.remove("banner-hidden");
        }
    }

    window.addEventListener("scroll", handleScroll);
});


let login = document.querySelector('.login-form');
let username_holder =

document.querySelector('#user-icon').onclick = () =>{
  login.classList.toggle('active');
}

window.onscroll = () =>{
  login.classList.remove('active');
}



let usernameInput = document.querySelector('input[name="username"]');
let passwordInput = document.querySelector('input[name="password"]');
let rememberCheckbox = document.getElementById('remember-me');

function saveCredentials() {
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

window.onload = function() {
  // When the page loads, check the saved credentials if any
  let savedUsername = getCookie('savedUsername');
  let savedPassword = getCookie('savedPassword');
  
  if (savedUsername && savedPassword) {
    // If the saved credentials are valid, fill in the form fields
    usernameInput.value = decodeURIComponent(savedUsername);
    passwordInput.value = decodeURIComponent(savedPassword);
    rememberCheckbox.checked = true;
  }
}