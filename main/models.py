from django.db import models
from login.models import Client, Restaurant


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=20, unique=True,)

    def __str__(self):
        return self.name


class Dish(models.Model):
    ingredients = models.ManyToManyField(
        Ingredient, related_name="dishes_with", blank=True
    )
    name = models.CharField(max_length=80)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="my_dishes"
    )
    price = models.FloatField()

    vegetarian = models.BooleanField()
    vegan = models.BooleanField()
    celiac = models.BooleanField()
    nuts_free = models.BooleanField()
    lactose_free = models.BooleanField()

    dish_image = models.ImageField(blank=True)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name


class Rating(models.Model):

    options = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    rate = models.IntegerField(choices=options)
    comment = models.CharField(max_length=300)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="user_ratings"
    )
    dish = models.ForeignKey(
        Dish, on_delete=models.CASCADE, related_name="dish_ratings"
    )
    date = models.DateField()

    def __str__(self):
        return "Comment from" + str(self.client) + " to " + str(self.dish)

    class Meta:
        unique_together = ("client", "dish")
