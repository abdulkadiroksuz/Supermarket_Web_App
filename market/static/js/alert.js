// Function to create and display a custom modal with an error message
function showErrorModal(errorMessage) {
    // Create modal container
    var modalContainer = document.createElement("div");
    modalContainer.className = "custom-modal";

    // Create modal content
    var modalContent = document.createElement("div");
    modalContent.className = "modal-content";

    // Create close button
    var closeButton = document.createElement("span");
    closeButton.className = "close-button";
    closeButton.innerHTML = "&times;"; // "×" symbol for close button
    closeButton.addEventListener("click", function () {
        document.body.removeChild(modalContainer);
    });

    // Create error message element
    var errorMessageElement = document.createElement("p");
    errorMessageElement.textContent = errorMessage;

    // Append elements to modal content
    modalContent.appendChild(closeButton);
    modalContent.appendChild(errorMessageElement);

    // Append modal content to modal container
    modalContainer.appendChild(modalContent);

    // Append modal container to the body
    document.body.appendChild(modalContainer);

    // Apply styles
    modalContainer.style.display = "flex";
    modalContainer.style.justifyContent = "center";
    modalContainer.style.alignItems = "center";
    modalContainer.style.position = "fixed";
    modalContainer.style.top = "0";
    modalContainer.style.left = "0";
    modalContainer.style.width = "100%";
    modalContainer.style.height = "100%";
    modalContainer.style.backgroundColor = "rgba(0,0,0,0.5)";
    modalContainer.style.zIndex = "9999999";

    modalContent.style.backgroundColor = "#fff";
    modalContent.style.margin = "auto auto";
    modalContent.style.padding = "20px";
    modalContent.style.borderRadius = "8px";
    modalContent.style.width = "fit-content";
    modalContent.style.boxShadow = "0 4px 8px rgba(0,0,0,0.1)";

    closeButton.style.position = "absolute";
    closeButton.style.top = "10px";
    closeButton.style.right = "10px";
    closeButton.style.fontSize = "25px";
    closeButton.style.cursor = "pointer";

    errorMessageElement.style.marginBottom = "0";
    errorMessageElement.style.marginRight = "1.5em";


    modalContainer.addEventListener("click", function (e) {
        if (e.target === modalContainer) {
            document.body.removeChild(modalContainer);
        }
    });
}