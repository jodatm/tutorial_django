from django.shortcuts import render
from .models import Estudiante
from .forms import EstudianteForm

# Create your views here.
def principal(request):
	estudiantes = Estudiante.objects.all()
	context = {
		"nombre":"Joshua",
		"estudiantes":estudiantes
	}
	return render(request,"estudiante/home.html", context)

def crear_estudiante(request):
	formulario = EstudianteForm()
	context = {
		"form": formulario
	}

	if request.POST:
		print(request.POST)
		formulario = EstudianteForm(request.POST)
		formulario.save()

	return render(request, "estudiante/crear_estudiante.html", context)