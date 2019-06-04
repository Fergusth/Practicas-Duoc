from django.contrib import admin
from .models import Usuarios, Rol, Alumno, Carrera, Practica, Carrera_escuela, Sede, Sede_Escuela, Escuela

admin.site.register(Usuarios)
admin.site.register(Rol)
admin.site.register(Alumno)
admin.site.register(Carrera)
admin.site.register(Practica)
admin.site.register(Carrera_escuela)
admin.site.register(Sede)
admin.site.register(Sede_Escuela)
admin.site.register(Escuela)