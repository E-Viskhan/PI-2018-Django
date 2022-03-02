from django.contrib.auth.models import AbstractUser
from django.db import models


class Photos(models.Model):
    small = models.CharField(max_length=8000)
    large = models.CharField(max_length=8000)


class CustomUser(AbstractUser):
    status = models.CharField(max_length=1024)
    photos = models.ForeignKey(Photos, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email