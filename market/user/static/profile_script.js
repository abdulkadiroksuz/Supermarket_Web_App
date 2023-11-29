// script.js
function showContent(contentId) {
    // Hide all content elements
    var contents = document.getElementsByClassName('content');
    for (var i = 0; i < contents.length; i++) {
        contents[i].classList.remove('show');
    }

    // Show the selected content
    document.getElementById(contentId).classList.add('show');
}


