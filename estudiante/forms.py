from django.forms import ModelForm
from django import forms
from .models import Estudiante

class EstudianteForm(ModelForm):

	class Meta:
		model = Estudiante
		fields = '__all__'
		labels = {
			'nombre': 'Nombre Completo',
			'ciudad': 'Ciudad residencia'
		}