"""geoservi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#esto es para utlizar la ruta a templates/media y que se guarden lass imagenes allá
from django.conf import settings
from django.conf.urls.static import static
from sucursales.views import sucursal, pagina3, pagina4, pagina5, ListarSucursales, home
from ubicarMapa.views import coordMapa, pagina1, UbicacionCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('searchll/', include('searchll.urls')),
    path('',home, name='home'),
    #Cuando referenciamos una clase de la vista en esta urle, se deme agregar asi: ListarProducto.as_View
    path('sucursal/', ListarSucursales.as_view(), name='sucursal'),
    path('pagina1/', pagina1, name='pagina1'),
    path('pagina3/', pagina3, name='pagina3'),
    path('pagina4/', pagina4, name='pagina4'),
    path('pagina5/', pagina5, name='pagina5'),
    path('coordMapa', coordMapa, name='coordMapa'),
    path('/Crear/', UbicacionCreateView.as_view(), name='crear'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
