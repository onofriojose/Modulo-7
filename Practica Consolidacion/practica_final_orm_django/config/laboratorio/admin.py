from django.contrib import admin

# Register your models here.
from .models import Laboratorio, Producto, DirectorGeneral

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')


class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'format_date', 'p_costo', 'p_venta')

    def format_date(self, obj):
        return obj.f_fabricacion.strftime('%Y')

    format_date.short_description = 'F FABRICACION'


admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)