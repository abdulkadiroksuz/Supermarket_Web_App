document.addEventListener('DOMContentLoaded', function () {
    var changePasswordButton = document.getElementById('changePasswordButton');
    if (changePasswordButton) {
      changePasswordButton.addEventListener('click', function () {
        $('#changePasswordCollapse').collapse('toggle');
      });
    }
  
    if (document.querySelectorAll('.change-password-form .alert-danger').length > 0) {
      $('#changePasswordCollapse').collapse('show');
    }
  });