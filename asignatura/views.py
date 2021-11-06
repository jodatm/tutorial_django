from django.shortcuts import render, redirect
from .models import Asignatura
from .forms import AsignaturaForm

# Create your views here.
def listar_asignatura(request):
	asignaturas = Asignatura.objects.all()
	context = {
		'asignaturas' : asignaturas
	}
	return render(request,'asignatura/lista_asignaturas.html', context)

def crear_asignatura(request):
	formulario = AsignaturaForm()
	context = {
		"form": formulario,
		"nombre": "Crear asignatura"
	}

	if request.POST:
		print(request.POST)
		formulario = AsignaturaForm(request.POST)
		formulario.save()
		return redirect('listar_asignatura')
	return render(request, 'asignatura/crear_asignatura.html', context)

def actualizar_asignatura(request, id):
	asignatura = Asignatura.objects.get(pk=id)
	formulario = AsignaturaForm(instance=asignatura)
	context = {
		"form" : formulario,
		"nombre": "Actualizar asignatura"
	}
	if request.POST:
		formulario = AsignaturaForm(request.POST, instance=asignatura)
		formulario.save()
		return redirect('listar_asignatura')
	return render(request, 'asignatura/crear_asignatura.html', context)

def eliminar_asignatura(request, id):
	if request.POST:
		asignatura = Asignatura.objects.get(pk=id)
		asignatura.delete()
		return redirect('listar_asignatura')
	return render(request, 'asignatura/eliminar_asignatura.html')