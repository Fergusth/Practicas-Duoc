from django.contrib import admin
from .models import (
    Usuarios, 
    Rol, 
    Alumno,
    Carrera,
    Practica,
    Sede,
    Sede_Escuela,
    Escuela,
    Practica_alumno,
    Supervisor_practica,
    Centro_practica,
    Profesor,
    asignatura_alumno
    )

admin.site.register(Usuarios)
admin.site.register(Rol)
admin.site.register(Alumno)
admin.site.register(Carrera)
admin.site.register(Practica)
admin.site.register(Sede)
admin.site.register(Sede_Escuela)
admin.site.register(Escuela)
admin.site.register(Practica_alumno)
admin.site.register(Supervisor_practica)
admin.site.register(Centro_practica)
admin.site.register(Profesor)
admin.site.register(asignatura_alumno)
