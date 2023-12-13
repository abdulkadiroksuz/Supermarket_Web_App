function searchProducts() {
    let search = document.getElementsByClassName("search-input")[0].value;
    if (search.length > 0) {
        window.location.href = "/search/" + search;
    }
    return false;
}

