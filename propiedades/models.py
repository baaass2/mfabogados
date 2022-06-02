from turtle import update
from django.db import models

# Create your models here.


class categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre_categoria

class propiedad(models.Model):

    nombre=models.CharField(max_length=50)
    precio=models.IntegerField(null=False)
    arriendo=models.BooleanField(blank=True,null=False)
    m2_terreno=models.FloatField(blank=True,null=True)
    m2_constru=models.FloatField(blank=True,null=True)
    n_hab=models.IntegerField(blank=True,null=True)
    n_baño=models.IntegerField(blank=True,null=True)
    descrip=models.TextField(blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)


    class Meta:
        verbose_name='propiedad'
        verbose_name_plural='propiedades'

    def __str__(self):
        return self.nombre

class imagenPropiedad(models.Model):
    imagen = models.ImageField(upload_to="propiedades")
    propiedad = models.ForeignKey(propiedad, on_delete=models.CASCADE, related_name='imagenes')



