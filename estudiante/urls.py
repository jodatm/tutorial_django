from django.urls import path
from . import views

urlpatterns = [
	path('lista', views.principal,name="lista_estudiantes"),
	path('crear', views.crear_estudiante,name="crear_estudiantes"),
	path('lista_asignaturas/<int:id>', views.listar_asignaturas,name="listar_asignaturas"),
	path('lista_asignaturas/crear_asignatura', views.lista_crear_asignaturas,name="lista_crear_asignaturas")
]