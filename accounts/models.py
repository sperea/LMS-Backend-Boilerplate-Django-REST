# accounts/models.py
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models

from . import managers # we will write this file shortly


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def __str__(self):
        return f"{self.email}'s custom account"


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    code = models.CharField(max_length=7, default="S" + uuid.uuid4().hex.upper()[0:6], blank=True,
                            verbose_name="Student code")

    def __str__(self):
        return self.user.get_username


class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    code = models.CharField(max_length=7, default="T" + uuid.uuid4().hex.upper()[0:6], blank=True,
                            verbose_name="Teacher code")

    def __str__(self):
        return self.user.get_username