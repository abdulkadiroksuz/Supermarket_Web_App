$(document).ready(function(){
    $('#user-icon').click(function(event){
        // Prevent the default action of the anchor tag
        event.preventDefault();
        // Toggle the display of the dropdown content
        $(this).next('.user-dropdown-content').slideToggle();
    });

    // Close the dropdown menu if the user clicks outside of it
    $(window).click(function(event) {
        if (!event.target.matches('#user-icon')) {
            $('.user-dropdown-content').slideUp();
        }
    });
});