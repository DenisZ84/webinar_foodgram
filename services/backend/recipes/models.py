from django.db import models
from users.models import User

from foodgram.contants import NAME_MAX_LENGTH


class RecipeQuerySet(models.QuerySet):
    def custom_count(self, user_id):
        self.count()


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Автор рецепта',
        related_name='recipes'
    )
    name = models.CharField(max_length=NAME_MAX_LENGTH,
                            verbose_name='Название рецепта')
    
    objects = RecipeQuerySet.as_manager()

    class Meta:
        ordering = ('name',)