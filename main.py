import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import platform
from datetime import datetime  # Importer le module datetime

# Vérifier le système d'exploitation
os_name = platform.system()
if os_name == "Windows":
    device = "cuda" if torch.cuda.is_available() else "cpu"
else:
    device = "mps" if torch.backends.mps.is_available() else "cpu"

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)

def generate_image(prompt):
    with torch.no_grad():
        image = pipe(prompt).images[0]
    return image

prompt = "a paiting of a mountain landscape with a river in the foreground"

generated_image = generate_image(prompt)

generated_image.show()

# Ajouter un timestamp au nom de l'image
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"generated_image_{timestamp}.png"

generated_image.save(filename)