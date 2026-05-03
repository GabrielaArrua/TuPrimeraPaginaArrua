from django.urls import path
from .views import registro
from django.contrib.auth.views import LoginView, LogoutView
from.views import registro, perfil, editar_perfil, CambiarPasswordView

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('editar-perfil/', editar_perfil, name='editar_perfil'),
    path('password/', CambiarPasswordView.as_view(), name='cambiar_password'),
]