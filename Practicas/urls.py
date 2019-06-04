from django.urls import path, include
from .views import listaUsuarios, crearUsuario
urlpatterns = [
    #Lista de Subjects
    path('usuarios/', listaUsuarios.as_view(), name="usuarios lista"),
    path('usuarios/crear/', crearUsuario.as_view(), name="usuarios crear"),
]