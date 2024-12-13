// Search user in subcription
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchInput').addEventListener('keyup', function() {
        let filter = this.value.toLowerCase();
        let rows = document.querySelectorAll('#userTableBody tr');

        rows.forEach(row => {
            let email = row.cells[1].textContent.toLowerCase();
            row.style.display = email.includes(filter) ? '' : 'none';
        });
    });
});