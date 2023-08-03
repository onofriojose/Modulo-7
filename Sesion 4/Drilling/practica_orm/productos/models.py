from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.precio}'