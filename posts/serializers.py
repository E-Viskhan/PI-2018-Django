from rest_framework import serializers

from posts.models import Post, PostPhotos
from profiles.models import Profile, Contacts, Photos


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPhotos
        fields = '__all__'
