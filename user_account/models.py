from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='e-mail')
    name = models.CharField(max_length=255, verbose_name='Nome')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Data de inscrição')
    is_staff = models.BooleanField(default=False, verbose_name='É da equipe')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
