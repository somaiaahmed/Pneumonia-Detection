document.getElementById('file-upload').addEventListener('change', function (event) {
    const file = event.target.files[0];

    if (file) {
        // Display the loader or processing message
        document.getElementById('diagnosis').innerText = "Processing...";
        document.getElementById('result-section').classList.remove('hidden');

        // Preview the uploaded image before sending to the server
        const reader = new FileReader();
        reader.onload = function (e) {
            const uploadedImage = document.getElementById('uploaded-image');
            uploadedImage.src = e.target.result; // Set the uploaded image as the src
        };
        reader.readAsDataURL(file); // Read the file as a data URL

        // Create a FormData object to send the image to the backend
        const formData = new FormData();
        formData.append('file', file);

        // Send the image to the backend (assuming Flask or Django)
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                // Show the diagnosis result and confidence score
                document.getElementById('diagnosis').innerText = data.prediction.diagnosis;
                document.getElementById('confidence').innerText = (data.prediction.confidence * 100).toFixed(2) + "%";
                document.getElementById('confidence-section').classList.remove('hidden');

                
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('diagnosis').innerText = "Error occurred. Please try again.";
            });
    }
});
