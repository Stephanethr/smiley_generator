import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import base64
from io import BytesIO
from django.http import JsonResponse
from django.shortcuts import render


# Fonction pour afficher la page index
def index(request):
    return render(request, 'image_generator/index.html')


# Fonction pour générer l'image via l'API
def generate_image_view(request):
    prompt = request.GET.get('prompt', '')

    if not prompt:
        return JsonResponse({'error': 'No prompt provided'}, status=400)

    # Charger et utiliser le modèle de génération d'image
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "CompVis/stable-diffusion-v1-4"
        pipe = StableDiffusionPipeline.from_pretrained(model_id)
        pipe = pipe.to(device)

        # Générer l'image
        with torch.no_grad():
            image = pipe(prompt).images[0]

        # Sauvegarder l'image en mémoire et la convertir en base64
        buffered = BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return JsonResponse({'image_data': img_str})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
