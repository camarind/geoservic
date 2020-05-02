
from django.forms import ModelForm
from ubicarMapa.models import Ubicacion

class UbicacionForm(ModelForm):
    # en la clase meta ponemos algunas propiedas
    class Meta:
        model= Ubicacion
        # Esto trae todos lod DAtos, sino en es un orde fields=['pub_date','headline', 'reporter']
        fields ='__all__'
        # sino quiero presentar un campo lo pongo asi: exclude=['nombreDelCampo']
