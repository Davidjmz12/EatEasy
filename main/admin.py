from django.contrib import admin
from .models import Dish, Ingredients, Rating

# Register your models here.
admin.site.register(Dish)
admin.site.register(Ingredients)
admin.site.register(Rating)
