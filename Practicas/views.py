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
    Sede,
    Sede_Escuela,
    Escuela,
    Carrera,
    Formulario_practica
)
from .serializer import (
    UsuarioSerializer, 
    PracticaAlumnoSerializer,
    sedeSerializer,
    sedeEscuelaSerializer,
    carreraSerializer,
    FormularioPracticaSerializer
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

@api_view(['POST'])
def listarCarrerasSede(request):
    """ Para listar carreras por sede, necesario para editar las prácticas 
        {"sede_id": 1}
    """
    idsede = request.data['sede_id']
    sede_escuelas = Sede_Escuela.objects.filter(sede__id=idsede)
    new_sede_escuelas = list()
    carreta_todas = list()

    for s_e in sede_escuelas:
        new_sede_escuelas.append(sedeEscuelaSerializer(s_e, context = {"request": request}).data)

    for n_e in new_sede_escuelas:
        carreras = Carrera.objects.filter(escuela__id=n_e['Escuela'])
        for c in carreras:
            carreta_todas.append(carreraSerializer(c, context = {"request": request}).data)

    return Response(carreta_todas)
    
@api_view(['POST'])
def editarHorasPractica(request):
    """ Para editar las horas de práctica de una sede y carrera, los tipos pueden ser 'Profesional' y 'Laboral'
        {"sede_id": 1, "carrera_id": 1, "tipo": "Profesional", "nuevas_horas": #}
    """
    sede_id = request.data['sede_id']
    carrera_id = request.data['carrera_id']
    tipo = request.data['tipo']
    nuevas_horas = request.data['nuevas_horas']

    practica = Practica.objects.get(sede__id=sede_id, carrera__id=carrera_id, tipoPractica=tipo)
    practica.cantidadHoras = nuevas_horas
    practica.save()

    return Response('Practica editada')

class crearUsuario(generics.CreateAPIView):
    queryset = Usuarios.objects.all()
    serializer_class = UsuarioSerializer

class crearSede(generics.CreateAPIView):
    queryset = Sede.objects.all()
    serializer_class = sedeSerializer

class crearCarrera(generics.CreateAPIView):
    queryset = Carrera.objects.all()
    serializer_class = carreraSerializer

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

class ListarPracticasPorEstado(generics.ListAPIView):
    serializer_class = PracticaAlumnoSerializer
    lookup_field = 'estado'

    def get_queryset(self):
        estado = self.kwargs.get('estado')
        return Practica_alumno.objects.filter(estado_practica = estado)

@api_view(['POST'])
def practicaDarDeBaja(request):
    """ Para dar de baja la práctica, hay que poner el id de la práctica_alumno
        {"pa_id": 1}
    """
    pa_id = request.data['pa_id']

    practica = Practica_alumno.objects.get(id=pa_id)
    practica.estado_practica = 'Anulada'
    practica.save()

    return Response('Practica dada de baja')

@api_view(['POST'])
def practicaDarDeAlta(request):
    """ Para dar de baja la práctica, hay que poner el id de la práctica_alumno
        {"pa_id": 1}
    """
    pa_id = request.data['pa_id']

    practica = Practica_alumno.objects.get(id=pa_id)
    practica.estado_practica = 'En curso'
    practica.save()

    return Response('Practica dada de alta')

def suma_dias_habiles(fecha_origen, dias):
    meses = dias/20

    return fecha_origen + timedelta(days=meses*30)

class Formulario_practicaView(viewsets.ModelViewSet):
    queryset = Formulario_practica.objects.all()
    serializer_class = FormularioPracticaSerializer