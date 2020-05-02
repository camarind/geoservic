from django.shortcuts import render
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from .models import Ubicacion
from django.urls import reverse

# Create your views here.. vista de la app ubicarMapa
def coordMapa(request):
    return  render(request, "coordMapa.html")

def pagina1(request):
    return render (request, "pag1.html")

#Creamos la clase con la misma nomenclatura
class UbicacionCreateView(CreateView):
    # Le decimos el modelo a trabajar
    model = Ubicacion
    # llamamos al formulario creado
    fields ='__all__'
    def get_success_url(self):
        return reverse('')
