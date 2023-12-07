import logging
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from recipes.pagination import CustomPageNumberPagination
from recipes.filters import RecipeFilter
from recipes.permissions import IsAuthorOrReadOnly
from recipes.models import Recipe, Ingredient
from recipes.serializers import RecipeSerializer, CreateRecipeSerializer, IngredientSerializer


logger = logging.getLogger(__name__)

class RecipeViewSet(ModelViewSet):
    #permission_classes = [AllowAny]
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilter
    pagination_class = CustomPageNumberPagination  # Указана в setting.py

    def get_queryset(self):
        logger.debug('Queryset started')
        queryset = Recipe.objects.all().select_related(
            'author').prefetch_related()
        return queryset

    def get_serializer_class(self):
        if self.action in ('create', 'update'):
            return CreateRecipeSerializer
        return RecipeSerializer
    

class IngredientViewSet(ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()