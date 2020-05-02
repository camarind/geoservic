from django.shortcuts import render

#utlizamos list View para listar
from django.views.generic.list import ListView
# importamos el modelo o los modelos que necesitamos para Listar
from .models import Sucursales

# Create your views here.


def sucursal(request):
    return  render (request, "sucursal.html")

def pagina3(request):
    return render (request, "pag3.html")

def pagina4(request):
    return render (request, "pag4.html")

def pagina5(request):
    return render (request, "pag5.html")


def home(request):
    return render (request, "home.html")

# Creamos una clase que hereda del ListView para poder todos los registros del model Producto
class ListarSucursales(ListView):
       # valla busque el templates la pagina1.html y meta todos los productos en esa pag1.html,
       #luego vamos a la urls global y agregamos la paginas allá
    template_name ='sucursal.html'
        # Este campo almacena el modelo Producto que se va a listar con Listview y lo importamos arriba
    model = Sucursales
