from django.db import models

from users.models import CustomUser


class Photos(models.Model):
    small = models.CharField(max_length=8000)
    large = models.CharField(max_length=8000)

    class Meta:
        verbose_name_plural = 'Photos'

    def __str__(self):
        return f'Photos {self.pk}'


class Contacts(models.Model):
    github = models.CharField(max_length=1000, null=True, blank=True)
    vk = models.CharField(max_length=1000, null=True, blank=True)
    facebook = models.CharField(max_length=1000, null=True, blank=True)
    instagram = models.CharField(max_length=1000, null=True, blank=True)
    twitter = models.CharField(max_length=1000, null=True, blank=True)
    website = models.CharField(max_length=1000, null=True, blank=True)
    youtube = models.CharField(max_length=1000, null=True, blank=True)
    mainLink = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.mainLink if self.mainLink else f'Contacts {self.pk}'

    class Meta:
        verbose_name_plural = 'Contacts'


class Profile(models.Model):
    status = models.CharField(max_length=1024)
    lookingForAJob = models.BooleanField(default=False)
    lookingForAJobDescription = models.CharField(max_length=1024)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    photos = models.ForeignKey(Photos, on_delete=models.SET_NULL, null=True, blank=True)
    contacts = models.ForeignKey(Contacts, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.user}'
