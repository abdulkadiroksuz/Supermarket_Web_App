$(document).ready(function(){
    $('#user-icon').click(function(event){
      // Toggle the display of the dropdown content
      $('.user-dropdown-content').slideToggle();
    });

    // Close the dropdown menu if the user clicks outside of it
    $(document).click(function(event) {
      if (!$(event.target).closest('#user-icon').length && !$(event.target).hasClass('user-dropdown-content')) {
        $('.user-dropdown-content').slideUp();
      }
    });

    // Prevent the dropdown from closing when clicking inside it
    $('.user-dropdown-content').click(function(event){
      event.stopPropagation();
    });
  });