from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=20)
    area = models.ForeignKey('storage.Area', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name.capitalize()} {self.user.last_name.capitalize()}"