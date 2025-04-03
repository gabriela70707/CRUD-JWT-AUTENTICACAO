from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    biografia = models.CharField(max_length=200, null=True, blank=True)
    idade = models.CharField(max_length=3, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=25, null=True, blank=True)
    escolaridade = models.CharField(max_length=30, null=True, blank=True)
    qnt_animais = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.username





