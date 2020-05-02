from django.db import models

# Create your models here.
"""un Continente pueden tener muchos paises
 pero un pais pertenece solo a  un continente."""
class Continentes(models.Model):
    """tabla Continentes."""
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

"""un idioma pueden tener muchos paises
 y un pais tener muchos idiomas."""
class Idiomas(models.Model):
    """ tabla Idiomas."""
    nom_idioma = models.CharField(max_length = 100)

    def __str__(self):
        return self.nom_idioma

class Paises(models.Model):
    """Tabla Paises ."""
    nom_pais = models.CharField(max_length = 100)
    cod_pais = models.CharField(max_length = 5)
    idioma_pais = models.ManyToManyField(Idiomas)
    continente_pais = models.ForeignKey(Continentes, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom_pais

class Departamentos(models.Model):
    nom_dpto = models.CharField(max_length = 100)
    pais_dpto = models.ForeignKey(Paises, null=False, on_delete=models.PROTECT)
    cod_dpto = models.CharField(max_length=4)

    def __str__(self):
        return self.nom_dpto

class Ciudades(models.Model):
    nom_ciudad = models.CharField(max_length=100)
    dpto_ciudad = models.ForeignKey(Departamentos, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom_ciudad

"""una red sociales pueden tener muchas empresas
 y un empresa tener muchas redes."""
class RedesSociales(models.Model):
    nom_red_social = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_red_social

class Estado(models.Model):
    nombre_estado = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre_estado

class Empresas(models.Model):
    nit = models.CharField(max_length=100)
    nombre_empresa = models.CharField(max_length=100)
    dir_empresa = models.CharField(max_length=100)
    tel_empresa = models.CharField(max_length=100)
    correo_empresa = models.EmailField()
    cant_sucursales = models.IntegerField()
    latitud_empresa = models.CharField(max_length=100)
    longitud_empresa = models.CharField(max_length=100)
    foto_empresa = models.FileField(null=True,upload_to='fotosEmpresa/%Y/%m/%d')
    red_sociales = models.ManyToManyField(RedesSociales)
    ciudad_empresa = models.ForeignKey(Ciudades, null=False, on_delete=models.PROTECT)
    dpto_empresa = models.ForeignKey(Departamentos, null=False, on_delete=models.PROTECT)
    pais_empresa = models.ForeignKey(Paises, null=False, on_delete=models.PROTECT)
    admin_empresa = models.CharField(max_length=100)
    descripcion_empresa = models.CharField(max_length=800)
    estado_empresa = models.ForeignKey(Estado, null=False, on_delete=models.PROTECT)
    archivo_mapaCiudad = models.FileField(null=True,upload_to='mapasEmpresa/%Y/%m/%d')
    sitio_web_empresa = models.URLField()

    def __str__(self):
        return self.nombre_empresa

class Mapas(models.Model):
    nombre_mapa = models.CharField(max_length=100)
    archivo_mapa =  models.FileField(null=True,upload_to='mapas/%Y/%m/%d')

    def __str__(self):
        return self.nombre_mapa

class Perfil(models.Model):
    nom_perfil = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_perfil

class Encargado(models.Model):
    nombre_encargado = models.CharField(max_length=100)
    apellido_encargado = models.CharField(max_length=100)
    cc_encargado = models.CharField(max_length=50)
    dir_encargado= models.CharField(max_length=120)
    cel_encargado = models.CharField(max_length=10)
    tel_emergencia = models.CharField(max_length=10)
    perfil_encargado = models.ForeignKey(Perfil, null=False, on_delete=models.PROTECT)
    foto_encarcado = models.FileField(null=True,upload_to='fotoEncargados/%Y/%m/%d')
    eps_encargado = models.CharField(max_length=100)
    arl_encargado = models.CharField(max_length=100)
    estado_encargadp = models.ForeignKey(Estado, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre_encargado

class Sucursales(models.Model):
    nit_sucursal = models.CharField(max_length=100)
    nom_sucursal = models.CharField(max_length=100)
    ciudad_sucursal = models.ForeignKey(Ciudades, null=False, on_delete=models.PROTECT)
    dpto_sucursal = models.ForeignKey(Departamentos, null=False, on_delete=models.PROTECT)
    pais_sucursal = models.ForeignKey(Paises, null=False, on_delete=models.PROTECT)
    empresa_sucursal = models.ForeignKey(Empresas, null=False, on_delete=models.PROTECT)
    dir_sucursal = models.CharField(max_length=100)
    tel_sucursal = models.CharField(max_length=100)
    descripcion_sucursal = models.CharField(max_length=800)
    encargado_sucursal = models.ForeignKey(Encargado, null=False, on_delete=models.PROTECT)
    foto_sucursal = models.FileField(null=True,upload_to='fotosSucursales/%Y/%m/%d')
    ruta_mapaSucursal = models.ForeignKey(Mapas, null=False, on_delete=models.PROTECT)
    estado_sucursal = models.ForeignKey(Estado, null=False, on_delete=models.PROTECT)
    sitio_web_sucursal = models.URLField()
    archivo_mapa_sucursal = models.FileField(null=True,upload_to='mapaSucursales/%Y/%m/%d')

    def __str__(self):
        return self.nom_sucursal
