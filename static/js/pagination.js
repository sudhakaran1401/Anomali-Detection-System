let currentPage = 1;
let rowsPerPage = 5;

function showPage(page) {
    const table = document.getElementById("dataTable");
    const tbody = table.getElementsByTagName("tbody")[0];
    const rows = tbody.getElementsByTagName("tr");

    const totalRows = rows.length;
    const totalPages = Math.ceil(totalRows / rowsPerPage) || 1;

    if (page < 1) page = 1;
    if (page > totalPages) page = totalPages;

    currentPage = page;

    for (let i = 0; i < totalRows; i++) {
        rows[i].style.display = "none";
    }

    const start = (currentPage - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    for (let i = start; i < end && i < totalRows; i++) {
        rows[i].style.display = "";
    }

    document.getElementById("pageInfo").innerText =
        `Page ${currentPage} of ${totalPages}`;

    document.getElementById("prevBtn").disabled = currentPage === 1;
    document.getElementById("nextBtn").disabled = currentPage === totalPages;
}

function changeRowsPerPage() {
    rowsPerPage = parseInt(document.getElementById("rowsSelect").value);
    currentPage = 1;
    showPage(currentPage);
}

function nextPage() {
    showPage(currentPage + 1);
}

function prevPage() {
    showPage(currentPage - 1);
}

document.addEventListener("DOMContentLoaded", function () {
    showPage(1);
});