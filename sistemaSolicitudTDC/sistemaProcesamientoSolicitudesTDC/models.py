from django.db import models

class Asignacion(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre + self.edad + self.nacionalidad



