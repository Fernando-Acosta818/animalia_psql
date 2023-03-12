from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    return render(request, 'index.html')

def animales(request):
    animales = Animal.objects.all()
    print(animales)
    context = {
        'animales' : animales
    }
    return render(request, 'animales.html', context)
