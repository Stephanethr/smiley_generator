from django.urls import path
from .views import generate_image_view

urlpatterns = [
    path('generate/', generate_image_view, name='generate_image'),
]