from django.shortcuts import render
from AppCoder.models import Avatar, Estudiantes, Curso, Profesor, Camada
from AppCoder.forms import EstudiantesForm, CursoForm, ProfesorForm, CamadaForm, UsuarioRegistro, FormularioEditar, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def inicioSesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contra)
            if user:
                login(request, user)
                return render(request, 'inicio.html')
        else:
            return render(request, 'padre.html', {'mensaje': 'Datos Incorrectos.'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'formulario': form})

def registro(request):
    if request.method == 'POST':
        form = UsuarioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'padre.html', {'mensaje': 'Usuario Creado.'})
    else:
        form = UsuarioRegistro()
    return render(request, 'registro.html', {'formulario': form})

@login_required
def cerrarSesion(request):
    logout(request)
    return render(request, 'padre.html', {'mensaje': 'Se ha cerrado sesión'})

@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == 'POST':
        form = FormularioEditar(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.set_password = info['password1']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.save()
            return render(request, 'inicio.html')
    else:
        form = FormularioEditar(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})
        return render(request, 'editar_perfil.html', {'formulario': form, 'usuario': usuario})

def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'inicio.html')
    else:
        return render(request, 'padre.html')
    
@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            usuarioActual = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'inicio.html')
    else:
        form = AvatarFormulario()
    return render(request, 'agregar_avatar.html', {'formulario': form})

@login_required
def buscar(request):
    return render(request, 'buscar.html')

@login_required
def crear_estudiante(request):
    if request.method == 'POST':
        formulario = EstudiantesForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nuevo = Estudiantes(
                nombre = dic['nombre'],
                apellido = dic['apellido'],
                email = dic['email'],
                edad = dic['edad']
            )
            nuevo.save()
            return render(request, 'inicio.html')
    else:
        formulario = EstudiantesForm()
    return render(request, 'crear_estudiantes.html', {'form': formulario})

@login_required
def crear_curso(request):
    if request.method == 'POST':
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nuevo = Curso(
                nombre = dic['nombre'],
                camada = dic['camada']
            )
            nuevo.save()
            return render(request, 'inicio.html')
    else:
        formulario = CursoForm()
    return render(request, 'crear_cursos.html', {'form': formulario})

@login_required
def crear_profesor(request):
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nuevo = Profesor(
                nombre = dic['nombre'],
                apellido = dic['apellido'],
                email = dic['email'],
                profesion = dic['profesion']
            )
            nuevo.save()
            return render(request, 'inicio.html')
    else:
        formulario = ProfesorForm()
    return render(request, 'crear_profesores.html', {'form': formulario})

@login_required
def crear_camada(request):
    if request.method == 'POST':
        formulario = CamadaForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            nuevo = Camada(
                numero = dic['numero'],
                profesor = dic['profesor'],
                cantidad_alumnos = dic['cantidad_alumnos']
            )
            nuevo.save()
            return render(request, 'inicio.html')
    else:
        formulario = CamadaForm()
    return render(request, 'crear_camada.html', {'form': formulario})

@login_required
def ver_estudiantes(request):
    if request.GET:
        if request.GET['nombre'] and request.GET['apellido']:
            nombre = request.GET['nombre']
            apellido = request.GET['apellido']
            estudiante = Estudiantes.objects.filter(nombre__icontains = nombre, apellido__icontains = apellido)
            mensaje = f"Estamos buscando al estudiante {nombre} {apellido}"
            return render(request, 'ver_estudiantes.html', {'mensaje': mensaje, 'resultados': estudiante})
        else:
            mensaje = "No se ha buscado nada"
            return render(request, 'ver_estudiantes.html', {'mensaje': mensaje})
    return render(request, 'ver_estudiantes.html')

@login_required
def ver_cursos(request):
    if request.GET:
        if request.GET['nombre']:
            nombre = request.GET['nombre']
            curso = Curso.objects.filter(nombre__icontains = nombre)
            mensaje = f"Estamos buscando el curso {nombre}"
            return render(request, 'ver_cursos.html', {'mensaje': mensaje, 'resultados': curso})
        else:
            mensaje = "No se ha buscado nada"
            return render(request, 'ver_cursos.html', {'mensaje': mensaje})
    return render(request, 'ver_cursos.html')

@login_required
def ver_profesores(request):
    if request.GET:
        if request.GET['nombre']:
            nombre = request.GET['nombre']
            profesor = Profesor.objects.filter(nombre__icontains = nombre)
            mensaje = f"Estamos buscando al profesor {nombre}"
            return render(request, 'ver_profesores.html', {'mensaje': mensaje, 'resultados': profesor})
        else:
            mensaje = "No se ha buscado nada"
            return render(request, 'ver_profesores.html', {'mensaje': mensaje})
    return render(request, 'ver_profesores.html')

@login_required
def ver_camadas(request):
    if request.GET:
        if request.GET['numero']:
            numero = request.GET['numero']
            camada = Camada.objects.filter(numero__icontains = numero)
            mensaje = f"Estamos buscando la camada {numero}"
            return render(request, 'ver_camadas.html', {'mensaje': mensaje, 'resultados': camada})
        else:
            mensaje = "No se ha buscado nada"
            return render(request, 'ver_camadas.html', {'mensaje': mensaje})
    return render(request, 'ver_camadas.html')

@login_required
def eliminar_estudiantes(request, nomEstudiante, apeEstudiante):
    estudiante = Estudiantes.objects.filter(nombre = nomEstudiante, apellido = apeEstudiante)
    estudiante.delete()
    mensaje = "Estudiante eliminado"
    return render(request, 'ver_estudiantes.html', {'mensaje': mensaje})

@login_required
def eliminar_cursos(request, nomCurso):
    curso = Curso.objects.get(nombre = nomCurso)
    curso.delete()
    mensaje = "Curso eliminado"
    return render(request, 'ver_cursos.html', {'mensaje': mensaje})

@login_required
def eliminar_profesores(request, nomProfesor, apeProfesor):
    profesor = Profesor.objects.filter(nombre = nomProfesor, apellido = apeProfesor)
    profesor.delete()
    mensaje = "Profesor eliminado"
    return render(request, 'ver_profesores.html', {'mensaje': mensaje})

@login_required
def eliminar_camada(request, numCamada):
    camada = Camada.objects.get(numero = numCamada)
    camada.delete()
    mensaje = "Camada eliminada"
    return render(request, 'ver_camadas.html', {'mensaje': mensaje})

@login_required
def editar_estudiantes(request, nomEstudiante, apeEstudiante):
    estudiante = Estudiantes.objects.get(nombre = nomEstudiante, apellido = apeEstudiante)
    if request.method == 'POST':
        formulario = EstudiantesForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            estudiante.nombre = dic['nombre']
            estudiante.apellido = dic['apellido']
            estudiante.email = dic['email']
            estudiante.edad = dic['edad']
            estudiante.save()
            return render(request, 'inicio.html')
    else:
        formulario = EstudiantesForm(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email, 'edad': estudiante.edad})
    return render(request, 'editar_estudiantes.html', {'form': formulario, 'nombre': nomEstudiante, 'apellido': apeEstudiante})

@login_required
def editar_cursos(request, nomCurso):
    curso = Curso.objects.get(nombre = nomCurso)
    if request.method == 'POST':
        formulario = CursoForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            curso.nombre = dic['nombre']
            curso.camada = dic['camada']
            curso.save()
            return render(request, 'inicio.html')
    else:
        formulario = CursoForm(initial={'nombre': curso.nombre, 'camada': curso.camada})
    return render(request, 'editar_cursos.html', {'form': formulario, 'nombre': nomCurso})

@login_required
def editar_profesores(request, nomProfesor, apeProfesor):
    profesor = Profesor.objects.get(nombre = nomProfesor, apellido = apeProfesor)
    if request.method == 'POST':
        formulario = ProfesorForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            profesor.nombre = dic['nombre']
            profesor.apellido = dic['apellido']
            profesor.email = dic['email']
            profesor.profesion = dic['profesion']
            profesor.save()
            return render(request, 'inicio.html')
    else:
        formulario = ProfesorForm(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
    return render(request, 'editar_profesores.html', {'form': formulario, 'nomre': nomProfesor, 'apellido': apeProfesor})

@login_required
def editar_camadas(request, numCamada):
    camada = Camada.objects.get(numero = numCamada)
    if request.method == 'POST':
        formulario = CamadaForm(request.POST)
        if formulario.is_valid():
            dic = formulario.cleaned_data
            camada.numero = dic['numero']
            camada.profesor = dic['profesor']
            camada.cantidad_alumnos = dic['cantidad_alumnos']
            camada.save()
            return render(request, 'inicio.html')
    else:
        formulario = CamadaForm(initial={'numero': camada.numero, 'profesor': camada.profesor, 'cantidad_alumnos': camada.cantidad_alumnos})
    return render(request, 'editar_camadas.html', {'form': formulario, 'numero': numCamada})

# Estudiantes
class ListaEstudiante(LoginRequiredMixin, ListView):
    model = Estudiantes

class DetalleEstudiante(LoginRequiredMixin, DetailView):
    model = Estudiantes

class CrearEstudiante(LoginRequiredMixin, CreateView):
    model = Estudiantes
    success_url = '/estudiante/list'
    fields = ['nombre', 'apellido', 'email', 'edad']

class ActualizarEstudiante(LoginRequiredMixin, UpdateView):
    model = Estudiantes
    success_url = '/estudiante/list'
    fields = ['nombre', 'apellido', 'email', 'edad']

class BorrarEstudiante(LoginRequiredMixin, DeleteView):
    model = Estudiantes
    success_url = '/estudiante/list'

# Curso
class ListaCurso(LoginRequiredMixin, ListView):
    model = Curso

class DetalleCurso(LoginRequiredMixin, DetailView):
    model = Curso

class CrearCurso(LoginRequiredMixin, CreateView):
    model = Curso
    success_url = '/curso/list'
    fields = ['nombre', 'camada']

class ActualizarCurso(LoginRequiredMixin, UpdateView):
    model = Curso
    success_url = '/curso/list'
    fields = ['nombre', 'camada']

class BorrarCurso(LoginRequiredMixin, DeleteView):
    model = Curso
    success_url = '/curso/list'

# Profesor
class ListaProfesor(LoginRequiredMixin, ListView):
    model = Profesor

class DetalleProfesor(LoginRequiredMixin, DetailView):
    model = Profesor

class CrearProfesor(LoginRequiredMixin, CreateView):
    model = Profesor
    success_url = '/profesor/list'
    fields = ['nombre', 'apellido', 'email', 'profesion']

class ActualizarProfesor(LoginRequiredMixin, UpdateView):
    model = Profesor
    success_url = '/profesor/list'
    fields = ['nombre', 'apellido', 'email', 'profesion']

class BorrarProfesor(LoginRequiredMixin, DeleteView):
    model = Profesor
    success_url = '/profesor/list'

# Camada
class ListaCamada(LoginRequiredMixin, ListView):
    model = Camada

class DetalleCamada(LoginRequiredMixin, DetailView):
    model = Camada

class CrearCamada(LoginRequiredMixin, CreateView):
    model = Camada
    success_url = '/camada/list'
    fields = ['numero', 'profesor', 'cantidad_alumnos']

class ActualizarCamada(LoginRequiredMixin, UpdateView):
    model = Camada
    success_url = '/camada/list'
    fields = ['numero', 'profesor', 'cantidad_alumnos']

class BorrarCamada(LoginRequiredMixin, DeleteView):
    model = Camada
    success_url = '/camada/list'