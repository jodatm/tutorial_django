from django.urls import path
from . import views

urlpatterns = [
	path('lista', views.principal,name="lista_estudiantes"),
	path('crear', views.crear_estudiante,name="crear_estudiantes")
]