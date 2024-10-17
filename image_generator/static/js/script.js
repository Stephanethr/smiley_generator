function generateImage() {
    const prompt = document.getElementById('prompt').value;
    const loader = document.getElementById('loader');

    if (!prompt) {
        alert('Please enter a prompt!');
        return;
    }

    // Afficher le loader
    loader.style.display = 'block';

    // Encode le prompt pour l'URL
    const encodedPrompt = encodeURIComponent(prompt);

    fetch(`/image-generator/generate/?prompt=${encodedPrompt}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Cacher le loader
            loader.style.display = 'none';

            if (data.error) {
                alert(data.error);
            } else {
                const imgContainer = document.getElementById('imageContainer');
                const img = document.createElement('img');
                img.src = 'data:image/png;base64,' + data.image_data;
                img.id = 'generatedImage';
                imgContainer.innerHTML = ''; // Vider le conteneur avant d'ajouter l'image
                imgContainer.appendChild(img);

                // Afficher le bouton de sauvegarde
                const saveBtn = document.getElementById('saveBtn');
                if (saveBtn) {
                    saveBtn.style.display = 'inline-block';
                }
            }
        })
        .catch(error => {
            // Cacher le loader en cas d'erreur
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
