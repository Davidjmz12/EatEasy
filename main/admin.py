from django.contrib import admin
from .models import Dish, Ingredient, Rating

# Register your models here.
admin.site.register(Dish)
admin.site.register(Ingredient)
admin.site.register(Rating)
