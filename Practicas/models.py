from django.db import models

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

class Carrera(models.Model):
    "Modelo de carrera"

    nombre = models.CharField(
        verbose_name = "nombre",
        max_length = 50,
    )

    duracionSemestres = models.IntegerField(
        verbose_name="duracion en semestres"
    )

    class Meta:
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return (self.nombre)

class Practica(models.Model):
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

    class Meta:
        verbose_name = "Practica"
        verbose_name_plural = "Practicas"

    def __str__(self):
        return (self.tipoPractica + " - " + self.carrera.nombre)

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
        max_length=20,
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return (self.nombre)

class Alumno(Usuarios):
    "Modelo alumno"

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return (self.nombre)

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

    ACEPTADA = "Aceptada"
    ANULADA = "Anulada"
    ASIGNADA = "Asignada"
    REPROBADA = "Reprobada"
    APROBADA = "Aprobada"
    ENVIADA = "Enviada"

    ESTADOS = (
        (ACEPTADA, "Aceptada"),
        (ANULADA, "Anulada"),
        (ASIGNADA, "Asignada"),
        (REPROBADA, "Reprobada"),
        (APROBADA, "Aprobada"),
        (ENVIADA, "Enviada")
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
        verbose_name="fecha inicio"
    )

    fecha_termino = models.DateField(
        verbose_name="fecha termino"
    )

    centro_practica = models.ForeignKey(
        Centro_practica,
        on_delete = models.CASCADE,
        verbose_name="centro de practica"
    )

    estado_practica = models.CharField(
        verbose_name="estado",
        choices=ESTADOS,
        default=ENVIADA,
        max_length = 50
    )
    
    class Meta:
        verbose_name = 'Practica_alumno'
        verbose_name_plural = "Practicas_alumno"
    
    def __str__(self):
        return (self.alumno.nombre)


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

class Carrera_escuela(models.Model):
    "Modelo carrera escuela"

    carrera = models.ForeignKey(
        Carrera,
        on_delete = models.CASCADE,
        verbose_name = "Carrera"
    )

    escuela = models.ForeignKey(
        Escuela,
        on_delete = models.CASCADE,
        verbose_name = "Escuela"
    )

    class Meta:
        verbose_name = "Carrera_escuela"
        verbose_name_plural = "Carreras_Escuelas"

    def __str__(self):
        return (self.carrera.nombre + " - " + self.escuela.nombre)

class Sede (models.Model):
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

class Sede_Escuela(models.Model):
    "Modelo de sede escuela"

    carrera = models.ForeignKey(
        Carrera,
        on_delete = models.CASCADE,
        verbose_name = "Carrera"
    )

    sede = models.ForeignKey(
        Sede,
        on_delete = models.CASCADE,
        verbose_name = "Escuela"
    )

    class Meta:
        verbose_name = "Sede_escuela"
        verbose_name_plural = "Sedes_Escuelas"

    def __str__(self):
        return (self.carrera.nombre + " - " + self.sede.nombre)

