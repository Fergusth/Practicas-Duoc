from rest_framework import serializers
from .models import (
    Usuarios, 
    Practica_alumno,
    Sede,
    Carrera
)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class PracticaAlumnoSerializer(serializers.ModelSerializer):
    fecha_inicio = serializers.DateField(format="%Y-%m-%d %H:%M:%S")
    fecha_termino = serializers.DateField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Practica_alumno
        fields = '__all__'

class sedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'

class carreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        field = '__all__'