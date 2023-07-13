import datetime
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria= models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5, verbose_name="Codigo producto")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    descripcion =models.TextField(max_length=200, blank=True, verbose_name="Descripcion")
    precio = models.IntegerField(blank=True, verbose_name="Precio")
    stock = models.IntegerField(blank=True, verbose_name="Stock")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.codigo

class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    total = models.BigIntegerField()
    fechaCompra = models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    usuario = models.CharField (max_length=40,blank=True,verbose_name="usuario")
    estado = models.TextField (max_length=40,blank=True,verbose_name="estado")
    

    def __str__(self):
        return str(self.id_boleta)


class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)