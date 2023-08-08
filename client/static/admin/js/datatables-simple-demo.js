window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }

    const datatablesIssue = document.getElementById('datatablesIssue');
        if (datatablesIssue) {
            new simpleDatatables.DataTable(datatablesIssue);
        }

//    const datatablesIssue = document.getElementById('datatablesIssue');
//        if (datatablesIssue) {
//           new simpleDatatables.DataTable(datatablesIssue);
//        }
});
