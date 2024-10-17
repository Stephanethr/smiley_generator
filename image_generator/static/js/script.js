function generateImage() {
    const prompt = document.getElementById('prompt').value;
    if (!prompt) {
        alert('Please enter a prompt!');
        return;
    }

    fetch(`/image-generator/generate/?prompt=${prompt}`)
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            const imgContainer = document.getElementById('imageContainer');
            const img = document.createElement('img');
            img.src = 'data:image/png;base64,' + data.image_data;
            img.id = 'generatedImage';
            imgContainer.innerHTML = '';
            imgContainer.appendChild(img);

            document.getElementById('saveBtn').style.display = 'inline-block';
        }
    })
    .catch(error => console.error('Error generating image:', error));
}

function saveImage() {
    const img = document.getElementById('generatedImage');
    const link = document.createElement('a');
    link.href = img.src;
    link.download = 'generated_image.png';
    link.click();
}
