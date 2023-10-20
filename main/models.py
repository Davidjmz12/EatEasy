from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=20)


class Dish(models.Model):
    ingredients = models.ManyToManyField(Ingredients, related_name="dishes_with", blank=True)
    name = models.CharField(max_length=20)


def validate_rate(value):
    if 0 <= value <= 5:
        return value
    else:
        raise ValidationError("The rating is a number between 1 and 5")


class Rating(models.Model):

    rate = models.IntegerField(validators=[validate_rate])
    comment = models.CharField(max_length=300)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="user_ratings")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="dish_ratings")
