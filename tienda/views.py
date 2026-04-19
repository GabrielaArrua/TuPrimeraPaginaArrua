from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, CategoriaForm, PostForm, BuscarProductoForm
from .models import Post

def inicio(request):
    return render(request, "tienda/inicio.html")

def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/productos/')
    return render(request, "tienda/form_producto.html", {"form": form})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "tienda/form_categoria.html", {"form": form})

def crear_post(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, "tienda/form_post.html", {"form": form})

def buscar_prodcuto(request):
    resultados = []
    if request.GET.get('nombre'):
        nombre = request.GET['nombre']
        resultados = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, "tienda/buscar.html", {"resultados": resultados})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, "tienda/productos.html", {"productos": productos})

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, "tienda/posts.html", {"posts": posts})