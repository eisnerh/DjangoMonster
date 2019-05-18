from django.db import models

# Create your models here.
from django.utils import timezone


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre_persona = models.CharField(max_length=200)
    apellido1_persona = models.CharField(max_length=200)
    apellido2_persona = models.CharField(max_length=200)
    edad_persona = models.IntegerField()
    telefono_persona = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_persona + ' ' + self.apellido1_persona

    class Meta:
        ordering = ['apellido1_persona']


class Mascota(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre_mascota = models.CharField(max_length=200)
    edad_mascota = models.IntegerField()
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    tipo_mascota = models.CharField(max_length=100, default='general')

    def __str__(self):
        return self.nombre_mascota


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
