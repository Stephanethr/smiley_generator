from django.urls import path
from .views import index, generate_image_view

urlpatterns = [
    path('', index, name='index'), # Route pour l'interface utilisateur
    path('generate/', generate_image_view, name='generate_image'), # API pour générer l'image
]
