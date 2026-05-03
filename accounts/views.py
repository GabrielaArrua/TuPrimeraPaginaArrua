from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Perfil
from .forms import RegistroForm, EditarPerfilForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {'form': form})


@login_required
def perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)

    return render(request, 'accounts/perfil.html', {
        'perfil': perfil
    })

@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = EditarPerfilForm(request.POST, request.FILES, instance=perfil)

        if form.is_valid():
            request.user.first_name = form.cleaned_data['first_name']
            request.user.last_name = form.cleaned_data['last_name']
            request.user.email = form.cleaned_data['email']
            request.user.save()

            form.save()

            return redirect('/accounts/perfil/')

    else:
        form = EditarPerfilForm(instance=perfil)

        form.fields['first_name'].initial = request.user.first_name
        form.fields['last_name'].initial = request.user.last_name
        form.fields['email'].initial = request.user.email

    return render(request, 'accounts/editar_perfil.html', {'form': form})

class CambiarPasswordView(PasswordChangeView):
    template_name = 'accounts/cambiar_password.html'
    success_url = reverse_lazy('perfil')