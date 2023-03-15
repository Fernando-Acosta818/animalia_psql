from django.shortcuts import render
from .models import Animal

def index(request):
    return render(request, 'index.html')

def animales(request):
    animales = Animal.objects.order_by('nombreAnimal')
    context = {
        'animales' : animales
    }
    return render(request, 'animales.html', context)

def animal(request, nombre):
    animal = Animal.objects.get(nombreAnimal = nombre.capitalize().replace("-", " "))
    context = {
        'animal' : animal
    }
    return render(request, 'animal.html', context)
