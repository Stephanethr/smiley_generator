import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import platform
from django.http import JsonResponse
from datetime import datetime
import base64
from io import BytesIO


os_name = platform.system()
device = "cuda" if os_name == "Windows" and torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to(device)

def generate_image(prompt):
    with torch.no_grad():
        image = pipe(prompt).images[0]
    return image

def generate_image_view(request):
    prompt = request.GET.get('prompt', '')
    if not prompt:
        return JsonResponse({'error': 'Prompt not provided'}, status=400)

    image = generate_image(prompt)
    
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return JsonResponse({'image_data': img_str})  