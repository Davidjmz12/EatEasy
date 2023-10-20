from django.contrib import admin
from .models import User, Client, Restaurant

# Register your models here.
admin.site.register(User)
admin.site.register(Client)
admin.site.register(Restaurant)


