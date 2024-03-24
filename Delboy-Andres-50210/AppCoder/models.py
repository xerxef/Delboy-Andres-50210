from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    edad = models.IntegerField()

class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    email = models.EmailField()
    profesion = models.CharField(max_length=60)

class Camada(models.Model):
    numero = models.IntegerField()
    profesor = models.CharField(max_length=60)
    cantidad_alumnos = models.IntegerField()

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
