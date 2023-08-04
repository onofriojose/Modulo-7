from django.urls import path
from .views import IndexPageView, listar_productos, editar_productos, crear_productos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('listar_productos/', listar_productos, name='listar_productos'),
    path('crear_productos/', crear_productos, name='crear_productos'),
    path('editar_productos/<int:productos_id>', editar_productos, name='editar_productos'),
]
