from django.db import models

# Create your models here.

class Remera(models.Model):
    modelo = models.CharField(max_length=20)
    talle = models.CharField(max_length=5)
    diseño = models.CharField(max_length=20)
    origen = models.CharField(max_length=20)
    
    def __str__(self):
        return f'El modelo es {self.modelo} con el diseño {self.diseño}, talle: {self.talle}. Origen: {self.origen}.'