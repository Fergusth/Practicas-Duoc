from django.db import models
from datetime import datetime
# Create your models here.

class Rol(models.Model):
    "Modelo del rol"

    descripcion = models.CharField(
        verbose_name="rol",
        max_length=50
    )

    class Meta:
        verbose_name = "rol"
        verbose_name_plural = "roles"

    def __str__(self):
        return (self.descripcion)

class Escuela(models.Model):
    "Model escuela"

    nombre = models.CharField(
        verbose_name = "nombre",
        max_length = 50
    )

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"

    def __str__(self):
        return (self.nombre)


class Carrera(models.Model):
    "Modelo de carrera"

    nombre = models.CharField(
        verbose_name = "nombre",
        max_length = 50,
    )

    duracionSemestres = models.IntegerField(
        verbose_name="duracion en semestres"
    )

    escuela = models.ForeignKey(
        Escuela,
        on_delete = models.CASCADE,
        verbose_name = "Escuela"
    )
    
    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return (self.nombre)


class Usuarios(models.Model):
    "Modelo de nota"

    rut = models.CharField(
        verbose_name="rut",
        max_length=20,
    )

    nombre = models.CharField(
        verbose_name="nombre",
        max_length=50,
    )

    rol = models.ForeignKey(
        Rol,
        on_delete=models.CASCADE,
        verbose_name = "rol",
    )

    email = models.CharField(
        verbose_name="correo electrónico",
        max_length=100,
    )

    contraseña = models.CharField(
        verbose_name="contraseña",
        default=".",
        max_length=20,
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return (self.nombre)

class Profesor(Usuarios):
    "Modelo profesor"

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "profesores"

    def __str__(self):
        return (self.nombre)

class Asignatura_inscrita(models.Model):
    "Modelo asignatura"

    descripcion = models.CharField(
        verbose_name = 'descripcion',
        max_length = 50
    )

    seccion = models.CharField(
        verbose_name = 'sección',
        max_length = 50
    )

    profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        verbose_name = 'Profesor'
    )

    class Meta:
        verbose_name = 'asignatura inscrita'
        verbose_name = 'asignaturas inscritas'
    
    def __str__(self):
        return (self.descripcion + " - " + self.seccion)

class Sede(models.Model):
    "Modelo sede"

    nombre = models.CharField(
        verbose_name = "nombre",
        max_length = 50,
    )

    ciudad = models.CharField(
        verbose_name = "ciudad",
        max_length = 50
    )

    telefono = models.IntegerField(
        verbose_name= "teléfono"
    )

    class Meta:
        verbose_name = "Sede"
        verbose_name_plural = "Sedes"

    def __str__(self):
        return (self.nombre)

class Practica(Asignatura_inscrita):
    "Modelo de práctica"
    
    PROFESIONAL = "Profesional"
    LABORAL = "Laboral"

    TIPOS_PRACTICA = (
        (PROFESIONAL, 'Profesional'),
        (LABORAL, 'Laboral')
    )

    tipoPractica = models.CharField(
        verbose_name = "tipo de practica",
        choices = TIPOS_PRACTICA,
        default = LABORAL,
        max_length = 20
    )

    cantidadHoras = models.IntegerField(
        verbose_name="cantidad de horas"
    )

    carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        verbose_name = "Carrera",
    )

    sede = models.ForeignKey(
        Sede,
        on_delete=models.CASCADE,
        verbose_name= "sede"
    )

    class Meta:
        verbose_name = "Practica"
        verbose_name_plural = "Practicas"

    def __str__(self):
        return (self.tipoPractica + " - " + self.carrera.nombre)

class Alumno(Usuarios):
    "Modelo alumno"

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return (self.nombre)

class asignatura_alumno(models.Model):
    """modelo asignatura del alumno"""

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        verbose_name = 'alumno'
    )

    asignatura_inscrita = models.ForeignKey(
        Asignatura_inscrita,
        on_delete=models.CASCADE,
        verbose_name = "Asignatura"
    )

    nota1 = models.IntegerField(
        verbose_name='Nota 1',
        blank=True,
        null=True
    )

    nota2 = models.IntegerField(
        verbose_name='nota 2',
        blank=True,
        null=True
    )

    nota3 = models.IntegerField(
        verbose_name='nota 3',
        blank=True,
        null=True
    )

    nota4 = models.IntegerField(
        verbose_name='nota 4',
        blank=True,
        null=True
    )

    promedio = models.IntegerField(
        verbose_name='Promedio',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Asignatura alumno"
        verbose_name_plural = "Asignaturas alumnos"

    def __str__(self):
        return (self.asignatura_inscrita.descripcion)


class Supervisor_practica(Usuarios):
    "modelo supervisor practica"

    cargo = models.CharField(
        max_length = 50,
        verbose_name = 'cargo'
    )

    class Meta:
        verbose_name = "Supervisor"
        verbose_name_plural = "Supervisores"

    def __str__(self):
        return (self.nombre)

class Centro_practica(models.Model):
    "modelo centro de práctica"

    rut = models.CharField(
        max_length=50,
        verbose_name ="rut"
    )

    nombre_empresa = models.CharField(
        max_length=50,
        verbose_name="nombre empresa"
    )

    direccion = models.CharField(
        max_length = 50,
        verbose_name = 'direccion'
    )
    
    supervisor = models.ForeignKey(
        Supervisor_practica,
        on_delete = models.CASCADE,
        verbose_name = "supervisor"
    )

    telefono = models.IntegerField(
        verbose_name="telefono"
    )

    horas_diarias = models.IntegerField(
        verbose_name="horas diarias de trabajo",
        default=8
    )

    class Meta:
        verbose_name = 'centro de practica'
        verbose_name_plural = 'centros de practica'
    
    def __str__(self):
        return (self.direccion)


class Practica_alumno(models.Model):
    "Modelo de practica asignada al alumno"

    EN_CURSO = "En curso"
    ANULADA = "Anulada"
    CERRADA = "Cerrada"
    INSCRITA = "Inscrita"
    
    ESTADOS = (
        (EN_CURSO, "En curso"),
        (ANULADA, "Anulada"),
        (CERRADA, "Cerrada"),
        (INSCRITA, "Inscrita")
    )

    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        verbose_name = "alumno"
    )

    practica = models.ForeignKey(
        Practica,
        on_delete=models.CASCADE,
        verbose_name = 'Práctica'
    )

    fecha_inicio = models.DateField(
        verbose_name="fecha inicio",
        blank=True,
        null=True
    )

    fecha_termino = models.DateField(
        verbose_name="fecha termino",
        blank=True,
        null=True
    )

    centro_practica = models.ForeignKey(
        Centro_practica,
        on_delete = models.CASCADE,
        verbose_name="centro de practica"
    )

    estado_practica = models.CharField(
        verbose_name="estado",
        choices=ESTADOS,
        default=INSCRITA,
        max_length = 50
    )
    
    class Meta:
        verbose_name = 'Practica_alumno'
        verbose_name_plural = "Practicas_alumno"
    
    def __str__(self):
        return (self.alumno.nombre)

class Sede_Escuela(models.Model):
    "Modelo de sede escuela"

    Escuela = models.ForeignKey(
        Escuela,
        on_delete = models.CASCADE,
        verbose_name = "escuela"
    )

    sede = models.ForeignKey(
        Sede,
        on_delete = models.CASCADE,
        verbose_name = "sede"
    )

    class Meta:
        verbose_name = "Sede_escuela"
        verbose_name_plural = "Sedes_Escuelas"

    def __str__(self):
        return (self.Escuela.nombre + " - " + self.sede.nombre)


class Formulario_practica(models.Model):
    
    alumno = models.ForeignKey(
        Alumno,
        on_delete = models.CASCADE,
        verbose_name = "alumno"
    )

    centro_practica = models.ForeignKey(
        Centro_practica,
        on_delete = models.CASCADE,
        verbose_name = "centro de practica"
    )

    fecha_inicio = models.DateField(
        verbose_name="fecha inicio",
        blank=True,
        null=True
    )


    class Meta:
        verbose_name = "Formulario_de_practica"
        verbose_name_plural = "Formularios_de_practica"

    def __str__(self):
        return (self.alumno.nombre + " - " + self.centro_practica.direccion)