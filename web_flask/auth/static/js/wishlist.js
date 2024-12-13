document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const properties = document.querySelectorAll('.property-item');
    let propertyIdToDelete = null; // Store the ID of the property to delete
    let propertyElementToDelete = null; // Store the DOM element to delete

    // Function to filter properties based on search input
    function filterProperties() {
        const searchTerm = searchInput.value.toLowerCase();

        properties.forEach(property => {
            const title = property.querySelector('.d-block.h5.mb-2').textContent.toLowerCase();
            property.style.display = title.includes(searchTerm) ? '' : 'none';
        });
    }

    // Search filter
    searchInput.addEventListener('keyup', filterProperties);

    // Delete property functionality with confirmation modal
    document.getElementById('propertyList').addEventListener('click', function(event) {
        if (event.target.closest('.delete-icon a')) {
            event.preventDefault();
            propertyIdToDelete = event.target.closest('.delete-icon a').getAttribute('data-id');
            propertyElementToDelete = event.target.closest('.property-item'); // Store the DOM element

            // Show the confirmation modal
            const deleteModal = new bootstrap.Modal(document.getElementById('deleteConfirmationModal'));
            deleteModal.show();
        }
    });

    // Confirm delete button in modal
    document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
        if (propertyIdToDelete) {
            // AJAX request to delete the property
            fetch(`/wishlist/delete_property/${propertyIdToDelete}`, {
                method: 'DELETE'
            })
            .then(response => {
                if (response.ok) {
                    console.log('Property deleted:', propertyIdToDelete);

                    // Remove the property from the DOM
                    if (propertyElementToDelete) {
                        propertyElementToDelete.remove();
                    }
                }
            })
            .catch(error => console.error('Error deleting property:', error))
            .finally(() => {
                // Clear stored property data after the deletion attempt
                propertyIdToDelete = null;
                propertyElementToDelete = null;
                
                // Reload the page after confirmation
                window.location.reload();
            });
        }
    });

    // Reload the page when the modal is dismissed
    const deleteConfirmationModal = document.getElementById('deleteConfirmationModal');
    deleteConfirmationModal.addEventListener('hidden.bs.modal', function() {
        window.location.reload();
    });

    filterProperties();
});
