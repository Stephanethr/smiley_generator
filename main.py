import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import platform

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


prompt = "a pepperoni pizza with a lot of cheese"

generated_image = generate_image(prompt)

generated_image.show()

generated_image.save("generated_image.png")
