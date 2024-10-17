function generateImage() {
    const prompt = document.getElementById('prompt').value;
    const loader = document.getElementById('loader');

    if (!prompt) {
        alert('Please enter a prompt!');
        return;
    }

    // Clear previous image and hide the save button
    const imgContainer = document.getElementById('imageContainer');
    imgContainer.innerHTML = '';  // Clear the container before generating the new image
    const saveBtn = document.getElementById('saveBtn');
    if (saveBtn) {
        saveBtn.style.display = 'none';
    }

    // Show the loader
    loader.style.display = 'block';

    // Encode the prompt for the URL
    const encodedPrompt = encodeURIComponent(prompt);

    // Fetch the generated image
    fetch(`/image-generator/generate/?prompt=${encodedPrompt}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Hide the loader
            loader.style.display = 'none';

            if (data.error) {
                alert(data.error);
            } else {
                const img = document.createElement('img');
                img.src = 'data:image/png;base64,' + data.image_data;
                img.id = 'generatedImage';
                imgContainer.appendChild(img);

                // Show the save button
                if (saveBtn) {
                    saveBtn.style.display = 'inline-block';
                }
            }
        })
        .catch(error => {
            // Hide the loader in case of an error
            loader.style.display = 'none';
            console.error('Error generating image:', error);
            alert('Error generating image. Please try again.');
        });
}

function saveImage() {
    const img = document.getElementById('generatedImage');
    if (!img) {
        alert('No image to save!');
        return;
    }

    const link = document.createElement('a');
    link.href = img.src;
    link.download = 'generated_image.png';
    link.click();
}
