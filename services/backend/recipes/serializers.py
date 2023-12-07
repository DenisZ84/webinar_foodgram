from rest_framework import serializers

from recipes.models import Recipe
from users.serializers import ProfileSerializers


class RecipeSerializer(serializers.ModelSerializer):
    author = ProfileSerializers(many=False)

    class Meta:
        model = Recipe
        fields = ('name', 'author')


class CreateRecipeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('name', 'author')