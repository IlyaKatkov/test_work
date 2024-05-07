from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import UserManager


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = 'пользователи'