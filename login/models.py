from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "admin"
        RESTAURANT = "RESTAURANT", "Restaurant"
        CLIENT = "CLIENT", "Client"

    role = models.CharField(max_length=10, choices=Role.choices, default=Role.ADMIN)
    avatar = models.ImageField(blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
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
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="Restaurants"
    )

    # New attributes for the restaurant.
    web_page = models.URLField(blank=True)
    precise_location = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    phone_number = models.IntegerField(blank=True, help_text="Contact phone number")
    description = models.CharField(max_length=300)
    rest_name = models.CharField(max_length=50)
    rest_image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username


class DeliveryPage(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="delivery_urls"
    )

    def __str__(self):
        return "Delivery " + str(self.name) + " of " + str(self.restaurant)
