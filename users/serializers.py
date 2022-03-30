from profiles.serializers import PhotosSerializer, StatusSerializer
from users.models import CustomUser
from rest_framework import serializers
from follows.models import Follow


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')

    photos = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    followed = serializers.SerializerMethodField()

    def get_photos(self, user):
        # profile = user.profile_set.first()
        photos = user.profile.photos
        return PhotosSerializer(photos).data

    def get_status(self, user):
        profile = user.profile
        return StatusSerializer(profile).data
    #photos
    # новый апп две модели, сериализаторы, добавить админку, связки двух моделей.
    # posts app -> post & image & post image nullable  & post [text, author: profile)
    # 5 - strange social network with only 5 posts a day
    # viewset ovverride create check posts a day posts have datefield
    # posts.objects.filter if posts more than 5 return exception


    def get_followed(self, user):
        me = self.context['request'].user
        if me.is_anonymous:
            return False

        return Follow.objects.filter(follower=me, followed=user).exists()

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'photos', 'status', 'followed']
