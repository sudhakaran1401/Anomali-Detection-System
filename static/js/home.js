
const fileInput = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");

fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
        fileName.style.display = "block";
        fileName.innerText = "Selected: " + fileInput.files[0].name;
    }
});

function showLoader() {
    document.getElementById("loader").style.display = "block";

    let btn = document.getElementById("submitBtn");
    if (btn) {
        btn.disabled = true;
        btn.innerText = "Processing...";
    }
}
