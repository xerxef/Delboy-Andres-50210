from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Login
    path('login/', inicioSesion, name='Login'),

    # Logout
    path('logout/', cerrarSesion, name='Logout'),

    # Editar
    path('editar_usuario/', editarUsuario, name='EditarUsuario'),

    # Registro
    path('register/', registro, name='SignUp'),

    # Avatar
    path('editar_avatar/', agregarAvatar, name='EditarAvatar'),

    # Acerca de mi
    path('about_me/', aboutMe, name='AboutMe'),

    # Inicio
    path('', inicio, name='Inicio'),
    
    # Creacion
    path('buscar/', buscar, name='Buscar'),
    path('estudiantes/', crear_estudiante, name='crearEstudiante'),
    path('curso/', crear_curso, name='crearCurso'),
    path('profesor/', crear_profesor, name='crearProfesor'),
    path('camada/', crear_camada, name='crearCamada'),

    # Busqueda
    path('ver_estudiantes/', ver_estudiantes, name='buscarEstudiante'),
    path('ver_cursos/', ver_cursos, name='buscarCurso'),
    path('ver_profesores/', ver_profesores, name='buscarProfesor'),
    path('ver_camadas/', ver_camadas, name='buscarCamada'),

    # Eliminacion
    path('eliminar_estudiante/<nomEstudiante>/<apeEstudiante>/', eliminar_estudiantes, name='eliminarEstudiantes'),
    path('eliminar_cursos/<nomCurso>/', eliminar_cursos, name='eliminarCursos'),
    path('eliminar_profesores/<nomProfesor>/<apeProfesor>/', eliminar_profesores, name='eliminarProfesores'),
    path('eliminar_camadas/<numCamada>/', eliminar_camada, name='eliminarCamada'),

    # Edicion
    path('editar_estudiantes/<nomEstudiante>/<apeEstudiante>/', editar_estudiantes, name='editarEstudiantes'),
    path('editar_cursos/<nomCurso>/', editar_cursos, name='editarCursos'),
    path('editar_profesores/<nomProfesor>/<apeProfesor>/', editar_profesores, name='editarProfesores'),
    path('editar_camadas/<numCamada>/', editar_camadas, name='editarCamadas'),

    # CRUD Clase Estudiante
    path('estudiante/list/', ListaEstudiante.as_view(), name='EstudianteLeer'),
    path('estudiante/<int:pk>/', DetalleEstudiante.as_view(), name='EstudianteDetalle'),
    path('estudiante/crear/', CrearEstudiante.as_view(), name='EstudianteCrear'),
    path('estudiante/editar/<int:pk>/', ActualizarEstudiante.as_view(), name='EstudianteEditar'),
    path('estudiante/borrar/<int:pk>/', BorrarEstudiante.as_view(), name='EstudianteEliminar'),

    # CRUD Clase Curso
    path('curso/list/', ListaCurso.as_view(), name='CursosLeer'),
    path('curso/<int:pk>/', DetalleCurso.as_view(), name='CursoDetalle'),
    path('curso/crear/', CrearCurso.as_view(), name='CursoCrear'),
    path('curso/editar/<int:pk>/', ActualizarCurso.as_view(), name='CursoEditar'),
    path('curso/borrar/<int:pk>/', BorrarCurso.as_view(), name='CursoEliminar'),

    # CRUD Clase Profesor
    path('profesor/list/', ListaProfesor.as_view(), name='ProfesorLeer'),
    path('profesor/<int:pk>/', DetalleProfesor.as_view(), name='ProfesorDetalle'),
    path('profesor/crear/', CrearProfesor.as_view(), name='ProfesorCrear'),
    path('profesor/editar/<int:pk>/', ActualizarProfesor.as_view(), name='ProfesorEditar'),
    path('profesor/borrar/<int:pk>/', BorrarProfesor.as_view(), name='ProfesorEliminar'),

    # CRUD Clase Camada
    path('camada/list/', ListaCamada.as_view(), name='CamadaLeer'),
    path('camada/<int:pk>/', DetalleCamada.as_view(), name='CamadaDetalle'),
    path('camada/crear/', CrearCamada.as_view(), name='CamadaCrear'),
    path('camada/editar/<int:pk>/', ActualizarCamada.as_view(), name='CamadaEditar'),
    path('camada/borrar/<int:pk>/', BorrarCamada.as_view(), name='CamadaEliminar'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)