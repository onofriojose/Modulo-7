from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'

# Controlador para listar productos
def listar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

# views para crear productos
def crear_productos(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST) # se catptura el formulario
        if form.is_valid(): # se valida el formulario
            form.save() # se guarda el formulario si es valido
            messages.success(request, 'Producto agregado correctamente')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Datos invalidost')
            return HttpResponseRedirect(reverse('crear_productos'))
    else:
        form = ProductosForm()
    return render(request, 'crear_productos.html', {'form': form})

def editar_productos(request, productos_id):
    book = get_object_or_404(Productos, id=productos_id)
    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=productos)
        if form.is_valid():
            productos = form.save(commit=False)  # guardamos y rescatamos producto
            productos.save()
            messages.success(request, 'Producto editado exitosamente')
            return redirect('listar_productos')
        else:
            messages.error(request, 'Error editando producto')
            return HttpResponseRedirect(reverse('editar_productos', args=[productos_id]))
    else:
        form = ProductosForm(instance=productos)
        return render(request, 'editar_productos.html', {'form': form, 'productos_id': productos_id})