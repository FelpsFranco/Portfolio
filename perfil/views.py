from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def experiencia(request):
    return render(request, 'experiencia.html')

def skils(request):
    return render(request, 'skils.html')
