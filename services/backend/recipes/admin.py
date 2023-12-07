from django.contrib import admin

from recipes.models import Recipe, IngredientAmount


class RecipeAmountAdmin(admin.TabularInline):
    model = IngredientAmount
    extra = 1
    min_num = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',
                    'get_ingredients', )
    list_filter = ('name',)
    inlines = (RecipeAmountAdmin,)

    @admin.display(description='Ингредиенты')
    def get_ingredients(self, obj):
        return '1'