from django.shortcuts import render
from rest_framework import  viewsets, generics
from .serializer import UsuarioSerializer
from .models import Usuarios
# Create your views here.

class listaUsuarios(generics.ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
    
class crearUsuario(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer