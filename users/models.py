from django.contrib.auth.models import AbstractUser
from django.db import models


class Photos(models.Model):
    small = models.CharField(max_length=8000)
    large = models.CharField(max_length=8000)

    class Meta:
        verbose_name_plural = 'Photos'


class CustomUser(AbstractUser):
    lookingForAJob = models.BooleanField(default=False)
    lookingForAJobDescription = models.CharField(max_length=1024)
    status = models.CharField(max_length=1024)
    photos = models.ForeignKey(Photos, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()