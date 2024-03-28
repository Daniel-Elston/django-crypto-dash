const card1viewChart = document.getElementById('card-1');
const card2viewChart = document.getElementById('card-2');
const card3viewChart = document.getElementById('card-3');
const cardLongviewChart = document.getElementById('card-long');
const dtsub = document.getElementById('dt-sub');
const datatable1 = document.getElementById('datatable1');

new Chart(card1viewChart, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Card 1',
            data: [65, 59, 80, 81, 56, 55, 40],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


new Chart(card2viewChart, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Card 2',
            data: [65, 59, 80, 81, 56, 55, 40],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});


new Chart(card3viewChart, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Card 3',
            data: [65, 59, 80, 81, 56, 55, 40],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

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
                    beginAtZero: true
                }
            }
        }
    })
});


new Chart(dtsub, {
    type: 'bar',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
            label: 'Card 4',
            data: [65, 59, 80, 81, 56, 55, 40],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const dataTable = new simpleDatatables.DataTable(datatable1, {
    searchable: true,
    fixedHeight: true,
    data: {
        headings: ['Name', 'Position', 'XOffice'],
    data: [
        ['test', 'Tiger Test Nixon', 'System Architect'],
        ['test', 'Tiger Nixon', 'System test'],
        ]
    }
});

dataTable.insert({
    data: [
        ['test', 'Tiger Nixon', 'System Architect'],
    ]
});
