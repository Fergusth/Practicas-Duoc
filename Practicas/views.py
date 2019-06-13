from django.shortcuts import render
from rest_framework import  viewsets, generics
from rest_framework import generics, views, status
from .serializer import UsuarioSerializer, PracticaAlumnoSerializer
from rest_framework.decorators import api_view, schema
from datetime import datetime, timedelta
from rest_framework.response import Response

from .models import (
    Usuarios,
    Practica,
    Practica_alumno,
    Alumno,
    Centro_practica,
    Sede
)
from .serializer import (
    UsuarioSerializer, 
    PracticaAlumnoSerializer,
    sedeSerializer
)

# Create your views here.

@api_view(['POST'])
def iniciarSesion(request):
    """
    Para usar api
    {"correo": "estecorreonoexiste@gmail.com", "contrasenia": "contrasenianoexiste"}
    """
    correo = request.data['correo']
    contrasenia = request.data['contrasenia']

    try:
        usuario = Usuarios.objects.get(email=correo, contraseña=contrasenia)
        usuarioRet = {
            "id": usuario.id,
            "rut": usuario.rut,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol": usuario.rol.descripcion
        }
        return Response(usuarioRet)
    except Usuarios.DoesNotExist:
        return Response('No existe este usuario', status=status.HTTP_404_NOT_FOUND)

class listaUsuarios(generics.ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

class listaSedes(generics.ListAPIView):
    queryset = Sede.objects.all()
    serializer_class = sedeSerializer

class crearUsuario(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

@api_view(['POST'])
def registrarPractica(request):
    """
    Para usar api
    Este sirve para registrar la práctica una vez aceptada la práctica
    { "id_alumno": 1, "id_practica": 1, "fecha_inicio": "2019-12-09", "id_centro_practica" : 1}
    """
    id_alumno = request.data['id_alumno']
    id_practica = request.data['id_practica']
    fecha_inicio = request.data['fecha_inicio']
    id_centro_practica = request.data['id_centro_practica']

    alumno = Alumno.objects.get(id=id_alumno)
    practica = Practica.objects.get(id=id_practica)
    centro_practica = Centro_practica.objects.get(id=id_centro_practica)

    num_dias =  int(round(practica.cantidadHoras/centro_practica.horas_diarias))
    print(num_dias)

    inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_termino = ''
    fecha_termino = suma_dias_habiles(inicio, num_dias).strftime('%Y-%m-%d')
    practica_alumno = Practica_alumno.objects.create(alumno=alumno, practica=practica, fecha_inicio = fecha_inicio, fecha_termino = fecha_termino, centro_practica = centro_practica)
    retorno = object()
    retorno = {
        "alumno":practica_alumno.alumno.id,
        "practica":practica_alumno.practica.id,
        "fecha_inicio":practica_alumno.fecha_inicio,
        "fecha_termino":practica_alumno.fecha_termino
    }

    return Response(retorno)
    
def suma_dias_habiles(fecha_origen, dias):
    meses = dias/20

    return fecha_origen + timedelta(days=meses*30)

