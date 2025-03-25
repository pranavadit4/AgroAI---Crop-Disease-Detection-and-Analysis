// Get the file input element
const fileInput = document.querySelector('input[type="file"]');

// Add an event listener for when the file input changes
fileInput.addEventListener('change', function () {
    const file = fileInput.files[0];

    // Check if a file is selected
    if (file) {
        const fileType = file.type;

        // Validate the file type
        if (!fileType.startsWith('image/')) {
            alert('Please upload a valid image file.');
            fileInput.value = ''; // Clear the input
        } else {
            alert(`Selected file: ${file.name}`);
        }
    }
});
