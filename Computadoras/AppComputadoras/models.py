from django.db import models


#-------------Modelo-Computadora---------#### 
class Computadora(models.Model):
    fabricante = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)

    def __str__(self):
        return self.fabricante + " " + str(self.marca)


#--------------Modelo Procesador------------#######
class Procesador(models.Model):
    nombre = models.CharField(max_length=50)
    numeroModelo = models.IntegerField()

    def __str__(self):
        return self.nombre + " " + str(self.numeroModelo)
        

#--------------Modelo Motherboard---------------#####
class Motherboard(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)

    def __str__(self):
        return self.marca+ " " + str(self.modelo)



