from django.contrib.auth.models import AbstractUser
from django.db import models

from foodgram.contants import EMAIL_MAX_LENGTH, USER_MAX_LENGTH


class User(AbstractUser):
    """Модель Пользователя."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    username = models.CharField(
        max_length=EMAIL_MAX_LENGTH, unique=True,
        verbose_name='Ник пользователя')
    email = models.EmailField(blank=False, unique=True,
                              verbose_name='Электронная почта')
    first_name = models.CharField('Имя', max_length=USER_MAX_LENGTH)
    last_name = models.CharField('Фамилия', max_length=USER_MAX_LENGTH)

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    pass