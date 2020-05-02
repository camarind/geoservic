from django.db import models

# Create your models here.
class PruebaDb(models.Model):
    nombre = models.CharField(max_length =120)
    descripcion = models.CharField(max_length = 120)

    def _str__(self):
        return self.nombre
