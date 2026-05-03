from django.urls import path
from .views import (
    inicio,
    buscar_producto,
    lista_posts,
    detalle_producto,
    about,
    ProductoListView,
    ProductoCreateView,
    ProductoDeleteView,
    ProductoUpdateView
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('buscar/', buscar_producto, name='buscar'),
    path('posts/', lista_posts, name='posts'),
    path('producto/<int:id>/', detalle_producto, name='detalle_producto'),
    path('productos/', ProductoListView.as_view(), name='productos'),
    path('crear-producto/', ProductoCreateView.as_view(), name='crear_producto'),
    path('about/', about, name='about'),
    path('producto/<int:pk>/editar/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('producto/<int:pk>/borrar/', ProductoDeleteView.as_view(), name='borrar_producto'),
]
