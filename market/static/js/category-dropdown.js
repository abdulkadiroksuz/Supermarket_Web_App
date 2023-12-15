function loadCategories(updateUrl) {
    let parent = document.getElementById('category-dropdown-menu');
    let dropdown = parent.getElementsByClassName('dropdown-content')[0];
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
