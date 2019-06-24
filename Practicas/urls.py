from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    listaUsuarios,
    crearUsuario,
    registrarPractica, 
    iniciarSesion,
    listaSedes,
    listarCarrerasSede,
    editarHorasPractica,
    crearCarrera,
    crearSede,
    ListarPracticasPorEstado,
    practicaDarDeBaja,
    practicaDarDeAlta,
    Formulario_practicaView,
    listarCentros,
    ListarCentrosId,
    listarSupervisores,
    SupervisorId,
    practicaView,
    ListarFormPracticas,
    editarFormPractica,
    addFormPractica
)

urlpatterns = [
    #Lista de Subjects
    path('iniciarSesion/', iniciarSesion, name="iniciar sesion"),
    path('usuarios/', listaUsuarios.as_view(), name="usuarios lista"),
    path('usuarios/crear/', crearUsuario.as_view(), name="usuarios crear"),
    path('usuarios/alumno/registrarPractica', registrarPractica, name="registrar practica"),
    path('sedes/lista/', listaSedes.as_view(), name="listaSedes"),
    path('centros/lista/', listarCentros.as_view(), name="listaSedes"),
    path('centros/<int:id>/', ListarCentrosId.as_view(), name="listaSedes"),
    path('supervisores/lista/', listarSupervisores.as_view(), name="listaSedes"),
    path('supervisores/<int:id>/', SupervisorId.as_view(), name="listaSedes"),
    path('carreras/lista/', listarCarrerasSede, name="listaCarrerasSede"),
    path('editarhoras/', editarHorasPractica, name="editarhoras"),
    path('carrera/crear/', crearCarrera.as_view(), name="creaCarrera"),
    path('sede/crear/', crearSede.as_view(), name="crearSede"),
    path('anular/', practicaDarDeBaja, name="anularPractica"),
    path('darAlta/', practicaDarDeAlta, name="darDeAltaPractica"),
    path('listar/practica-alumno/estado/<estado>/', ListarPracticasPorEstado.as_view(), name="listarPracticaEstado"),
    path('formularioPractica/', Formulario_practicaView.as_view({'get': 'list', 'post': 'create'}), name="formularioPractica"),
    path('formularioPractica/<int:pk>/', Formulario_practicaView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update','delete': 'destroy'}), name="formularioPractica"),
    path('asignatura/', practicaView.as_view({'get': 'list', 'post': 'create'}), name="formularioPractica"),
    path('asignatura/<int:pk>/', practicaView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update','delete': 'destroy'}), name="formularioPractica"),
    path('formPractica/<rutAlumno>/', ListarFormPracticas, name="listaSedes"),
    path('formPracticaEditar/<rutAlumno>/<fechaInicio>/', editarFormPractica, name="listaSedes"),
    path('formPracticaAgregar/<rutAlumno>/<fechaInicio>/<centro>', addFormPractica, name="listaSedes"),
]