from django_filters.rest_framework import (AllValuesMultipleFilter,
                                           BooleanFilter, FilterSet, filters)

from recipes.models import Recipe


class RecipeFilter(FilterSet):
    class Meta:
        model = Recipe
        fields = []