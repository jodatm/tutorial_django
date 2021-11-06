from django.db import models

# Create your models here.
class Asignatura(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=10)
	creditos = models.IntegerField(default=4)

	def __str__(self):
		return self.nombre