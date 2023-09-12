from django.forms import ModelForm
from .models import tareas, Libro

class FormularioTareas(ModelForm):
    class Meta:
        model = tareas
        fields = ['titulo', 'descripcion', 'importante']

class LibroForm(ModelForm):
    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'imagen','descripcion']
        