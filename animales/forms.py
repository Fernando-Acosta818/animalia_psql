from django.forms import ModelForm
from .models import Animal

class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
