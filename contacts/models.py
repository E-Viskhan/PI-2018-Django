from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    city = models.CharField(max_length=30)

    street = models.CharField(max_length=50)

    house = models.CharField(max_length=50)

    flat = models.IntegerField(max_length=10)

    zip_code = models.IntegerField(max_length=20)


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    Address = models.ForeignKey(Address, on_delete=models.CASCADE, default='')
