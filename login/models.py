from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        RESTAURANT = "RESTAURANT", "Restaurant"
        CLIENT = "CLIENT", "Client"

    base_role = Role.ADMIN

    role = models.CharField(max_length=10, choices=Role.choices)
    avatar = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class ClientManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)


class Client(User):
    base_role = User.Role.CLIENT
    clients = ClientManager()

    class Meta:
        proxy = True


class RestaurantManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.CLIENT)


class Restaurant(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="Restaurants")

    # New attributes for the restaurant.
    web_page = models.URLField(blank=True)
    precise_location = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.user.username


class DeliveryPage(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="delivery_urls")


# class Restaurant(User):
#     base_role = User.Role.RESTAURANT
#
#     # New attributes for the restaurant.
#     web_page = models.URLField(blank=True)
#     precise_location = models.CharField(max_length=100)
#     city = models.CharField(max_length=20)
#     phone_number = models.IntegerField()
#
#     restaurants = RestaurantManager()
#
#     class Meta:
#         proxy = True


class Ingredients(models.Model):
    name = models.CharField(max_length=20)


class Dish(models.Model):
    ingredients = models.ManyToManyField(Ingredients, related_name="dishes_with", blank=True)
    name = models.CharField(max_length=20)


class Rating(models.Model):

    @staticmethod
    def validate_rate(value):
        if 0 <= value <= 5:
            return value
        else:
            raise ValidationError("The rating is a number between 1 and 5")

    rate = models.IntegerField(validators=[validate_rate])
    comment = models.CharField(max_length=300)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="user_ratings")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="dish_ratings")
