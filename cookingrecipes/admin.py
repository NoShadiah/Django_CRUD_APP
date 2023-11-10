from django.contrib import admin
from cookingrecipes.models import Recipe

admin.site.register(Recipe)
admin.site.site_header = "Recipes Admin"
admin.site.site_title = "Recipes Admin Portal"
admin.site.index_title = "Welcome to the Recipes management portal"