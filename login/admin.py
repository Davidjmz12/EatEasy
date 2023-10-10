from django.contrib import admin
from .models import User, Client, Restaurant, Dish, Ingredients, Rating

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Ingredients)
admin.site.register(Rating)

