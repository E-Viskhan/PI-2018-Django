from django.db import models
from users.models import CustomUser


class Address(models.Model):
    city = models.CharField(max_length=30)

    street = models.CharField(max_length=50)

    house = models.CharField(max_length=50)

    flat = models.IntegerField(null=True, blank=True)

    zip_code = models.IntegerField()

    def __str__(self):
        return f'{self.house} {self.street} {self.city}'


class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    phone = models.CharField(max_length=30)

    created_at = models.DateTimeField(auto_now_add=True)

    address = models.ForeignKey(Address, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.user}'
