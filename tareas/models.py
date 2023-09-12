from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tareas(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    fechacompleto = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' creado por ' + self.user.username
    
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, verbose_name="Título")
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción", null=True)

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

class cuentas_banco(models.Model):
    banco = models.CharField(max_length=250)
    nivel_1 = models.CharField(max_length=250)
    nivel_2 = models.CharField(max_length=250)
    nivel_3 = models.CharField(max_length=250)
    nivel_4 = models.CharField(max_length=250)
    anio_mes = models.CharField(max_length=250)
    valor = models.CharField(max_length=250)

    def __str__(self):
        fila = "Banco: " + self.banco + " - " + "nivel_1: " + self.nivel_1 + "nivel_2: " + self.nivel_2 + "nivel_3: " + self.nivel_3 + "nivel_4: " + self.nivel_4 + "anio_mes: " + self.anio_mes + "valor: " + self.valor
        return fila