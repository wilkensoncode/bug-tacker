window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesDev = document.getElementById('datatablesDev');
    if (datatablesDev) {
        new simpleDatatables.DataTable(datatablesDev);
    }

    const datatablesIssue = document.getElementById('datatablesIssue');
    if (datatablesIssue) {
        new simpleDatatables.DataTable(datatablesIssue);
    }


});
