from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('lista', views.listar_asignatura,name="listar_asignatura"),
	path('crear', views.crear_asignatura,name="crear_asignatura"),
	path('actualizar/<int:id>', views.actualizar_asignatura,name="actualizar_asignatura"),
	path('eliminar/<int:id>', views.eliminar_asignatura,name="eliminar_asignatura"),
]
