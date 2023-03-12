from django.forms import ModelForm
from .models import *

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['nombreAnimal', 'descripcion', 'foto1', 'foto2', 'foto3', 'foto4', 'foto5', 'habitat']
        labels = {
            'nombreAnimal' : 'Nombre del animal',
            'descripcion' : 'Descripción',
            'foto1' : 'Foto 1',
            'foto2' : 'Foto 2',
            'foto3' : 'Foto 3',
            'foto4' : 'Foto 4',
            'foto5' : 'Foto 5',
            'habitat' : 'Hábitat'
        }
        
class FiloForm(ModelForm):
    class Meta:
        model = Filo
        fields = '__all__'

class ClaseForm(ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'
        
class OrdenForm(ModelForm):
    class Meta:
        model = Orden
        fields = '__all__'
        
class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'
        
class FamiliaForm(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'

class EspecieForm(ModelForm):
    class Meta:
        model = Especie
        fields = '__all__'
        
class ConservacionForm(ModelForm):
    class Meta:
        model = Conservacion
        fields = '__all__'