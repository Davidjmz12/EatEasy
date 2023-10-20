from django.db import models
from login.models import Client
from django.core.exceptions import ValidationError

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=20)


class Dish(models.Model):
    ingredients = models.ManyToManyField(Ingredients, related_name="dishes_with", blank=True)
    name = models.CharField(max_length=20)


class Rating(models.Model):

    rate = models.IntegerField()
    comment = models.CharField(max_length=300)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="user_ratings")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="dish_ratings")
