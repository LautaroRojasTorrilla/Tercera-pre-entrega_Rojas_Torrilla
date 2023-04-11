from django.db import models

# Create your models here.

class Remera(models.Model):
    modelo = models.CharField(max_length=20)
    talle = models.CharField(max_length=5)
    disenio = models.CharField(max_length=20)
    origen = models.CharField(max_length=20)
    
    def __str__(self):
        return f'El modelo es "{self.modelo}" con diseño de "{self.disenio}", talle: "{self.talle}". Origen: "{self.origen}".'
    
# class Remera(models.Model):
#     modelo = models.CharField(max_length=20)
#     talle = models.CharField(max_length=5)
#     diseño = models.CharField(max_length=20)
#     origen = models.CharField(max_length=20)

#     def __str__(self):
#         table = "| {:<10} | {:<5} | {:<20} | {:<20} |\n".format("Modelo", "Talle", "Diseño", "Origen")
#         table += "| {:<10} | {:<5} | {:<20} | {:<20} |\n".format("-"*10, "-"*5, "-"*20, "-"*20)
#         table += "| {:<10} | {:<5} | {:<20} | {:<20} |\n".format(self.modelo, self.talle, self.diseño, self.origen)
#         table += "\n"
#         return table
#hice esta clase, pero no se veía correctamente en el admin. Supongo que es una limitacion de la visualizacion.