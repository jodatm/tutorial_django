from django.db import models

# Create your models here.
class Estudiante(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=10)
	edad = models.IntegerField(default=15)
	ciudad = models.CharField(max_length=75, default="Tuluá")
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre