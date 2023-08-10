from datetime import date
from django.core.validators import MinValueValidator
from django.db import models
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.nombre}'

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}'
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField(validators=[MinValueValidator(limit_value=date(2015, 1, 1))])
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.nombre}'
