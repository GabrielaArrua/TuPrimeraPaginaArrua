from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('crear-producto/', crear_producto),
    path('crear-categoria/', crear_categoria),
    path('crear-post/', crear_post),
    path('buscar/', buscar_prodcuto),
    path('productos/', lista_productos),
    path('posts/', lista_posts, name='posts'),
]
