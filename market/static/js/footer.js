function updateFooter(updateUrl) {
    $.ajax({
        type: "GET",
        url: updateUrl,
        success: function (data) {
            let phone = document.getElementById('footer-phone');
            let email = document.getElementById('footer-email');
            let address = document.getElementById('footer-address');

            phone.innerText = "Phone : " + data.company_phone;
            email.innerText = "Email : " + data.company_email;
            address.innerText = "Address : " + data.company_address;


        },
    });
}
