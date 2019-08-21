from django.db import models

# Create your models here.

class Persona(models.Model):
    #Si no pones nada te crea un ID autoincremental
    nombre = models.CharField(max_length = 50)
    sexo = models.CharField(max_length = 10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()