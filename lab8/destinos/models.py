from django.db import models

class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to='pics')
    precioTour = models.IntegerField()
    ofertaTour = models.BooleanField(default=False)
