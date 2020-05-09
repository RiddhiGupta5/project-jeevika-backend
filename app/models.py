from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    is_staff = models.BooleanField(default=False)       # Field necessary for a django user
    is_active = models.BooleanField(default=True)       # Field necessary for a django user
    is_superuser = models.BooleanField(default=False)   # Field necessary for a django user

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_no']

    objects = CustomUserManager()

    def __str__(self):
        return self.email