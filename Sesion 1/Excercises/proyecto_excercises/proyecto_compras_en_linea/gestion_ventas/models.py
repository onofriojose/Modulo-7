from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=50)
    celular = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
    
class Producto(models.Model):
    nombre = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
    def __str__(self):
        return f'{self.nombre} - {self.categoria}'
    
class Compra(models.Model):
    numero = models.IntegerField(max_digits=10)
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
    
    def __str__(self):
        return f'{self.numero} - {self.fecha} - {self.monto}'