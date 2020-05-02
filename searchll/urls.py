from django.urls import path
from searchll.views  import searchll_listar

urlpatterns = [
    path('listar/', searchll_listar, name='listar'),
]
