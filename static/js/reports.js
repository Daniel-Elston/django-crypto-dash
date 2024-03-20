const dataTable = new simpleDatatables.DataTable(datatable1, {
    searchable: true,
    fixedHeight: true,
    data: {
        headings: ['Name', 'Position', 'Office'],
    data: [
        ['test', 'Tiger Nixon', 'System test'],
        ['test', 'Tiger Nixon', 'System Architect'],
        ]
    }
});

dataTable.insert({
    data: [
        ['test', 'Tiger Nixon', 'System Architect'],
    ]
});

// const datatable1 = document.getElementById('datatable1');

// fetch('/total_views')
// .then(res => res.json())
// .then (data => {
//     const dataTable = new simpleDatatables.DataTable(datatable1, {
//         searchable: true,
//         fixedHeight: true,
//         data: {
//             headings: data.labels,
//         data: data.data
//         }
//     })
// });
