from django.db import models
# sirve para crear formularios a partir de Modelos
# se importan las librerias
import folium
# pedir lugar para geolocalizar
from geopy.geocoders import Nominatim
import time
import math
# Create your models here.
#Modelo para recibir coordenadas de latitud y longitud
class Ubicacion(models.Model):
    nombre = models.CharField(max_length = 200)
    latitud = models.CharField(max_length = 50)
    longitud = models.CharField(max_length = 50)
    fecha = models.DateTimeField(auto_now_add = True)
    descripcion = models.CharField(max_length = 200, blank = True, null = True, default= "")
    #para impirmi el objeto Ubicacion que nos muestre el nombre
    def __str__(self):
        return self.nombre



# al diseñar esto se proce a hacer las migraciones por consola para la base de DAtos....
