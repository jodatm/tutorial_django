from django.db import models
from asignatura.models import Asignatura

# Create your models here.
class Estudiante(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=10)
	edad = models.IntegerField(default=15)
	ciudad = models.CharField(max_length=75, default="Tuluá")
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre

class EstudianteAsignatura(models.Model):
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

	def __str__(self):
		return self.estudiante.nombre + " " + self.asignatura.nombre

