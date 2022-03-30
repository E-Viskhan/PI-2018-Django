from django.db import models

# Create your models here.
# photos
# новый апп две модели, сериализаторы, добавить админку, связки двух моделей.
# posts app -> post & image & post image nullable  & post [text, author: profile)
# 5 - strange social network with only 5 posts a day
# viewset ovverride create check posts a day posts have datefield
# posts.objects.filter if posts more than 5 return exception
from profiles.models import Profile


class PostPhotos(models.Model):
    small = models.CharField(max_length=8000)
    large = models.CharField(max_length=8000)

    class Meta:
        verbose_name_plural = 'Post photos'

    def __str__(self):
        return f'Post photos {self.pk}'


class Post(models.Model):
    title = models.TextField(max_length=100)
    text = models.TextField(max_length=10000)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    photos = models.ForeignKey(PostPhotos, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Post {self.title}'
