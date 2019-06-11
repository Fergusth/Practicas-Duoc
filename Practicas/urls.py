from django.urls import path, include
from .views import listaUsuarios, crearUsuario, registrarPractica
urlpatterns = [
    #Lista de Subjects
    path('usuarios/', listaUsuarios.as_view(), name="usuarios lista"),
    path('usuarios/crear/', crearUsuario.as_view(), name="usuarios crear"),
    path('usuarios/alumno/registrarPractica', registrarPractica, name="registrar practica")
]