document.addEventListener('DOMContentLoaded', (event) => {
    const deleteButtons = document.querySelectorAll('.btn-outline-danger');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {

            alert('The address will be deleted!');
        });
    });
});


