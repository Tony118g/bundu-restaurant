
// Waits for document to load before calling functions
document.addEventListener("DOMContentLoaded", function() {
    hideMessage();
});

// Hides any displayed message after 3 seconds
function hideMessage() {
    let message = document.getElementById("msg");

    if (message) {
        setTimeout(function(){ 
            message.style.display = "none"; 
            }, 3000);
    }
}