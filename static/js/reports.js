const datatable1 = document.getElementById('datatable1');

fetch('/reports_api')
.then(res => res.json())
.then (data => {
    const dataTable = new simpleDatatables.DataTable(datatable1, {
        searchable: true,
        fixedHeight: true,
        data: {
            headings: data.labels,
        data: data.data
        }
    })
});
