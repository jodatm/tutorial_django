from django.shortcuts import render, redirect
from .models import Estudiante, EstudianteAsignatura
from .forms import EstudianteForm, EstudianteAsignaturaForm

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

def listar_asignaturas(request, id):
	estudiante = Estudiante.objects.get(pk=id)
	asignaturas = EstudianteAsignatura.objects.filter(estudiante=estudiante)
	print
	context = {
		"asignaturas":asignaturas
	}
	return render(request, "estudiante/listar_asignatura.html", context)

def lista_crear_asignaturas(request):
	formulario = EstudianteAsignaturaForm()
	context = {
		"form": formulario
	}
	if request.POST:
		formulario = EstudianteAsignaturaForm(request.POST)
		formulario.save()
		return redirect('lista_estudiantes')
	return render(request, "estudiante/listar_asignatura_estudiante.html", context)