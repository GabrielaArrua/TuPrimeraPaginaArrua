from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, CategoriaForm, PostForm, BuscarProductoForm
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

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

def buscar_producto(request):
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

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, "tienda/detalle_producto.html", {"producto": producto})

class ProductoListView(ListView):
    model = Producto
    template_name = 'tienda/productos.html'
    context_object_name = 'productos'


class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'marca', 'descripcion', 'precio', 'categoria', 'imagen']
    template_name = 'tienda/form_producto.html'
    success_url = reverse_lazy('productos')

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'marca', 'descripcion', 'precio', 'categoria', 'imagen']
    template_name = 'tienda/form_producto.html'
    success_url = reverse_lazy('productos')
    login_url = '/accounts/login/'


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    template_name = 'tienda/borrar_producto.html'
    success_url = reverse_lazy('productos')
    login_url = '/accounts/login/'

def about(request):
    return render(request, 'tienda/about.html')