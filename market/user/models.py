from django.db import models
from django.contrib.auth.models import User

class Area(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name.capitalize()}, {self.surname.capitalize()}"