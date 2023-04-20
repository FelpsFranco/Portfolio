from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiencia', views.experiencia, name='experiencia'),
    path('skils', views.skils, name='skils')
]
