from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from foodgram.contants import NAME_MAX_LENGTH, MIN_VALIDATION, MAX_VALIDATION


class Ingredient(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH, verbose_name='Название ингредиента')


class RecipeQuerySet(models.QuerySet):
    def custom_count(self, user_id):
        return self.count()


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


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент',
        null=True, )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество',
        validators=[
            MinValueValidator(
                MIN_VALIDATION,
                message='Количество ингредиентов должно быть дольше нуля'
            ),
            MaxValueValidator(MAX_VALIDATION, message='Слишком много!')
        ]
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, verbose_name='Рецепт',
        related_name='recipe_ingredients'
    )

    class Meta:
        ordering = ('recipe',)
        verbose_name = 'ингредиент'