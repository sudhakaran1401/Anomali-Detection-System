
let chartType = 'bar';

const normal = JSON.parse(document.getElementById('normal-data').textContent);
const anomalies = JSON.parse(document.getElementById('anomaly-data').textContent);

let chart;

function renderChart() {
    if (chart) chart.destroy();

    chart = new Chart(document.getElementById('chartCanvas'), {
        type: chartType,
        data: {
            labels: ['Normal', 'Anomalies'],
            datasets: [{
                label: "Records",
                data: [normal, anomalies],
                backgroundColor: ['#28a745', '#dc3545'],
                borderRadius: 10
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: "Anomaly Detection Overview"
                },
                legend: { display: false }
            }
        }
    });
}

renderChart();

function toggleChart() {
    chartType = chartType === 'bar' ? 'pie' : 'bar';
    renderChart();
}

const scatterElement = document.getElementById('scatter-data');
let scatterData = [];

if (scatterElement) {
    scatterData = JSON.parse(scatterElement.textContent);
}

if (scatterData.length === 0) {
    document.getElementById('scatterChart').parentElement.innerHTML =
        "<p class='text-center text-muted'>No data available for scatter plot</p>";
} else {
    const normalPoints = scatterData.filter(d => d.label !== 'Anomaly');
    const anomalyPoints = scatterData.filter(d => d.label === 'Anomaly');

    new Chart(document.getElementById('scatterChart'), {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Normal',
                    data: normalPoints,
                    backgroundColor: '#28a745'
                },
                {
                    label: 'Anomalies',
                    data: anomalyPoints,
                    backgroundColor: '#dc3545'
                }
            ]
        },
        options: {
            plugins: {
                title: {
                    display: true,
                    text: "Anomaly Distribution"
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return "X: " + context.raw.x + ", Y: " + context.raw.y;
                        }
                    }
                }
            }
        }
    });
}

function toggleDark() {
    document.getElementById('body').classList.toggle('dark-mode');
}

function searchTable() {
    let input = document.getElementById("searchInput").value.toLowerCase();
    let rows = document.querySelectorAll("#dataTable tbody tr");

    rows.forEach(row => {
        row.style.display = row.innerText.toLowerCase().includes(input) ? "" : "none";
    });
}

function showAnomalies() {
    let rows = document.querySelectorAll("#dataTable tbody tr");

    rows.forEach(row => {
        row.style.display = row.innerText.includes("Anomaly") ? "" : "none";
    });
}

function downloadCSV() {
    let rows = document.querySelectorAll("table tr");
    let csv = [];

    rows.forEach(row => {
        let cols = row.querySelectorAll("td, th");
        let data = [];
        cols.forEach(col => data.push(col.innerText));
        csv.push(data.join(","));
    });

    let blob = new Blob([csv.join("\n")], { type: "text/csv" });
    let url = window.URL.createObjectURL(blob);

    let a = document.createElement("a");
    a.href = url;
    a.download = "data.csv";
    a.click();
}
