from django.db import models

from login.models import User


# Create your models here.

class Notification(models.Model):
    emissor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_sent_not")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_received_not")
    description = models.CharField(max_length=200)
    title = models.CharField(max_length=30)
    read = models.BooleanField(default=False)
    date = models.TimeField(auto_now=True)

    def __str__(self):
        return "Notification from " + str(self.emissor) + " to " + str(self.receiver) + " called " + self.title