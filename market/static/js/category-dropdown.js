function loadCategories(updateUrl) {
    let parent = document.getElementById('category-dropdown-menu');
    let dropdown = parent.getElementsByClassName('category-dropdown-content')[0];
    $.ajax({
        type: "GET",
        url: updateUrl,
        success: function (response) {
            if (response.success) {
                let categories = response.data;
                console.log(categories);
                for (let i = 0; i < categories.length; i++) {
                    var aElement = document.createElement('a');
                    aElement.setAttribute('href', categories[i].url);
                    aElement.innerText = categories[i].name;
                    dropdown.appendChild(aElement);
                }
            } else {
                showErrorModal(response.error);
            }
        },
    });
}

$(document).ready(function(){
    $('#category-title').click(function(event){
        // Toggle the display of the dropdown content
        $('.category-dropdown-content').slideToggle();
    });

    // Close the dropdown menu if the user clicks outside of it
    $(document).click(function(event) {
        if (!$(event.target).closest('#category-title').length && !$(event.target).hasClass('category-dropdown-content')) {
            $('.category-dropdown-content').slideUp();
        }
    });

    // Prevent the dropdown from closing when clicking inside it
    $('.category-dropdown-content').click(function(event){
        event.stopPropagation();
    });
});
