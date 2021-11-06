from django.forms import ModelForm
from django import forms
from .models import Estudiante, EstudianteAsignatura

class EstudianteForm(ModelForm):

	class Meta:
		model = Estudiante
		fields = '__all__'
		labels = {
			'nombre': 'Nombre Completo',
			'ciudad': 'Ciudad residencia'
		}

class EstudianteAsignaturaForm(ModelForm):

	class Meta:
		model = EstudianteAsignatura
		fields = '__all__'
		labels = {
			'estudiante': 'Nombre de estudiante',
			'asignatura': 'Nombre de asignatura'
		}