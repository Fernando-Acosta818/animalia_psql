from django.shortcuts import render, redirect
from .models import Animal
from .forms import AnimalForm

def index(request):
    return render(request, 'index.html')

def animales(request):
    return render(request, 'animales.html')

def registrar(request):
    #form = AnimalForm
    #context = {'form' : form}

    return render(request, 'registrar.html')
