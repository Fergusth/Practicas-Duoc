from django.urls import path, include
from .views import (
    listaUsuarios,
    crearUsuario,
    registrarPractica, 
    iniciarSesion,
    listaSedes
)

urlpatterns = [
    #Lista de Subjects
    path('iniciarSesion/', iniciarSesion, name="iniciar sesion"),
    path('usuarios/', listaUsuarios.as_view(), name="usuarios lista"),
    path('usuarios/crear/', crearUsuario.as_view(), name="usuarios crear"),
    path('usuarios/alumno/registrarPractica', registrarPractica, name="registrar practica"),
    path('sedes/lista/', listaSedes.as_view(), name="listaSedes")
]