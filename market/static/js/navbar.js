document.querySelector('.right-nav .user').addEventListener('click', function() {
    var dropdownContent = document.querySelector('.right-nav .user-dropdown-content');

    // Calculate the position based on the button's position
    var rect = this.getBoundingClientRect();
    var topPosition = rect.bottom + window.scrollY;
    var rightPosition = window.innerWidth - rect.right;

    // Apply the calculated position
    dropdownContent.style.top = topPosition + 'px';
    dropdownContent.style.right = rightPosition + 'px';

    // Toggle the show class
    dropdownContent.classList.toggle('show');
});
