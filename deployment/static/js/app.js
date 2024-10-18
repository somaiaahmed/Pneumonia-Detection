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
            uploadedImage.classList.remove('hidden');
        };
        reader.readAsDataURL(file); // Read the file as a data URL

        // Create a FormData object to send the image to the backend
        const formData = new FormData();
        formData.append('file', file);

        // Send the image to the backend 
        fetch('/pneumonia-detection', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                // Show the diagnosis result and confidence score
                const diagnosisText = document.getElementById('diagnosis');
                const confidenceText = document.getElementById('confidence');
                const confidenceSection = document.getElementById('confidence-section');

                // Set the diagnosis text
                diagnosisText.innerText = data.prediction.diagnosis;

                // Set the confidence score
                confidenceText.innerText = data.prediction.confidence;
                confidenceSection.classList.remove('hidden');

                // Set the color based on the diagnosis
                if (data.prediction.diagnosis === "Normal") {
                    diagnosisText.style.color = "green";  // Normal result
                } else if (data.prediction.diagnosis === "Pneumonia") {
                    diagnosisText.style.color = "red";    // Pneumonia result
                }
            })
            .catch(error => {
                console.error('Error:', error);
                document.getElementById('diagnosis').innerText = "Error occurred. Please try again.";
            });
    }
});
