from django.urls import path
from .views import index, generate_image_view

urlpatterns = [
    # Route pour l'interface utilisateur
    path('', index, name='index'),
    # API pour générer l'image
    path('generate/', generate_image_view, name='generate_image'),
]
