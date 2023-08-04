from django.contrib import admin

# Register your models here.
from .models import Productos, Fabrica

# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'fabrica')
    
class FabricaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


admin.site.register(Fabrica, FabricaAdmin)
admin.site.register(Productos, ProductosAdmin)