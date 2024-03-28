
const cardLongviewChart = document.getElementById('card-long');

fetch('/visuals_api')
.then(res => res.json())
.then (data => {
    new Chart(cardLongviewChart, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'Card 4',
                data: data.data,
                borderWidth: 1,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: false
                }
            }
        }
    })
});
