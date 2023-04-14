from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('perfil.urls')),
    path('admin/', admin.site.urls),
]
