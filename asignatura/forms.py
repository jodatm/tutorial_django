from django.forms import ModelForm
from django import forms
from .models import Asignatura

class AsignaturaForm(ModelForm):

	class Meta:
		model = Asignatura
		fields = '__all__'
		labels = {
			'nombre': 'Nombre de la asignatura',
		}