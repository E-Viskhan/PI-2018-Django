from django.db import models

from users.models import CustomUser


class Contacts(models.Model):
    github = models.CharField(max_length=1000)
    vk = models.CharField(max_length=1000)
    facebook = models.CharField(max_length=1000)
    instagram = models.CharField(max_length=1000)
    twitter = models.CharField(max_length=1000)
    website = models.CharField(max_length=1000)
    youtube = models.CharField(max_length=1000)
    mainLink = models.CharField(max_length=1000)

    def __str__(self):
        return self.mainLink

    class Meta:
        verbose_name_plural = 'Contacts'


class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
