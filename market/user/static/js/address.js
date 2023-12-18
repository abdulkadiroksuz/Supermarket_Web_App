document.addEventListener('DOMContentLoaded', (event) => {
    const deleteButtons = document.querySelectorAll('.btn-outline-danger');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {

            alert('The address will be deleted!');
        });
    });
});


$('#addressModal').on('hidden.bs.modal', function () {
    // Form alanlarını temizle
    $(this).find('form').trigger('reset');

    // Modal başlığını ve buton metnini varsayılana çevir
    $('#addressModalLabel').text('Add new address');
    $('#addressModal button[type="submit"]').text('Save').attr('name', 'add_address');

    // Herhangi bir hata mesajını temizle
    $(this).find('.alert').remove();
});

$('.new-address button').click(function() {
    // Form alanlarını sıfırla ve modal başlığını ayarla
    $('#addressModal form').trigger('reset');
    $('#addressModalLabel').text('Add new address');

    // Buton metnini ve özniteliklerini ayarla
    $('#addressModal button[type="submit"]').text('Save').attr('name', 'add_address');

    // Herhangi bir hata mesajını temizle
    $('#addressModal').find('.alert').remove();
});

