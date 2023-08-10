#  Por medio de la consola interpretador de python (shell), realice las siguientes consultas:
#  ○ Obtenga todos los objetos tanto Laboratorio, DirectorGeneral y Productos.
from laboratorio.models import Laboratorio, DirectorGeneral, Producto

# Obtener todos los objetos de las clases
laboratorios = Laboratorio.objects.all()
directores = DirectorGeneral.objects.all()
productos = Producto.objects.all()

print("Laboratorios:")
for laboratorio in laboratorios:
    print(laboratorio)

print("\nDirectores Generales:")
for director in directores:
    print(director)

print("\nProductos:")
for producto in productos:
    print(producto)


#  ○ Obtenga el laboratorio del Producto cuyo nombre es ‘Producto 1’.
producto = Producto.objects.get(nombre='Producto 1')
laboratorioProducto = producto.laboratorio
print("Laboratorio del Producto 'Producto 1':", laboratorioProducto)

#  ○ Ordene todos los productos por nombre, y que muestre los valores de nombre y
#  laboratorio.
productos = Producto.objects.order_by('nombre')
for producto in productos:
    print("Nombre:", producto.nombre)
    print("Laboratorio:", producto.laboratorio)
    
#  ○ Realice una consulta que imprima por pantalla los laboratorios de todos los productos.
productos = Producto.objects.all().select_related('laboratorio')
for producto in productos:
    print("Nombre del Producto:", producto.nombre)
    print("Laboratorio:", producto.laboratorio)
