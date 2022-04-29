from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    tipo = models.CharField(max_length=28)
    
    def __str__(self):
        return self.tipo
        
class Producto(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.tipo

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=20)
    def __str__(self):
        return self.tipo
        

class Usuario(models.Model):

    nombre = models.CharField(max_length=20)
    usuario = models.CharField(max_length=15)
    apellido = models.CharField(max_length=25)
    email = models.EmailField(max_length=70)
    rut = models.IntegerField()
    password = models.CharField(max_length=10)
    direccion = models.CharField(max_length=30)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario
    
   
class HistorialCompra(models.Model):
    estado = models.CharField(max_length=20)
    def __str__(self):
        return self.estado


class Suscripcion(models.Model):
    suscrito = models.BooleanField()
    email = models.EmailField(max_length=70)
    def __str__(self):
        return self.email
