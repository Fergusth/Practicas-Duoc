from django.shortcuts import render
from rest_framework import  viewsets, generics
from .serializer import UsuarioSerializer
from rest_framework.decorators import api_view, schema
from datetime import datetime, timedelta
from rest_framework.response import Response

from .models import (
    Usuarios,
    Practica,
    Practica_alumno,
    Alumno,
    Centro_practica,
)

# Create your views here.

class listaUsuarios(generics.ListAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer
    
class crearUsuario(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

@api_view(['POST'])
def registrarPractica(request):
    """
    Para usar api
    { "id_alumno": 11, "id_practica": 5, "fecha_inicio": "2019-12-09", "id_centro_practica" :  1}
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
    fecha_termino = suma_dias_habiles(inicio, num_dias)
    practica_alumno = Practica_alumno.objects.create(alumno=alumno, practica=practica, fecha_inicio = fecha_inicio, fecha_termino = fecha_termino, centro_practica = centro_practica)
    return Response(practica_alumno)
    
def suma_dias_habiles(fecha_origen, dias):
    meses = dias/20

    return fecha_origen + timedelta(days=meses*30)