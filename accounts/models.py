from django.db import models
from django.contrib.auth.models import User

class Perfil (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    
