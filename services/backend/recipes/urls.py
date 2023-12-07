from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import RecipeViewSet, IngredientViewSet

router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')
router.register('ingredient', IngredientViewSet, basename='ingredients1')

urlpatterns = [
    path('', include(router.urls)),
]