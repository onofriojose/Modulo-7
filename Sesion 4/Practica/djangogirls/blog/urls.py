from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('agregar/', views.agregarregistro, name='agregar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
]