from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('image-generator/', include('image_generator.urls')),  # Inclusion des URLs de l'app image_generator
]
