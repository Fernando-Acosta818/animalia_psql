from django.shortcuts import render
from .models import Animal
import random

def index(request):
    animal = Animal.objects.get(id = random.randint(1, len(Animal.objects.all())))

    desc = animal.descripcion
    if len(desc) > 800 :
        desc = desc[:800] + '...'

    context = {
        'animal' : animal,
        'desc' : desc
    }
    return render(request, 'index.html', context)

def nosotros(request):
    return render(request, 'nosotros.html')

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
