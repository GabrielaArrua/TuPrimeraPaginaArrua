from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):

    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'})
    )

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}),
        help_text=""
    )

    password2 = forms.CharField(
        label="Repetir contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repetir contraseña'}),
        help_text=""
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

from django import forms
from .models import Perfil

class EditarPerfilForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'fecha_de_nacimiento']

        widgets = {
            'fecha_de_nacimiento': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
