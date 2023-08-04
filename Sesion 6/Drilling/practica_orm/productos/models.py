from django.db import models

# Create your models here.

class Fabrica(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100, null=True, blank=True)  # nuevo campo para drilling sesion 5
    def __str__(self) -> str:
        return f'{self.nombre} - {self.pais}'

class Productos(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    # Sesion 5 Modulo 7
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE, blank=True, null=True)
    f_vencimiento = models.DateField(blank=True, null=True)   # nuevo campo para drilling sesion 5
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.precio}'

