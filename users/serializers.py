from users.models import CustomUser, Photos
from rest_framework import serializers
from follows.models import Follow


class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    photos = PhotosSerializer()

    followed = serializers.SerializerMethodField()

    def get_followed(self, user):
        me = self.context['request'].user
        if me.is_anonymous:
            return False

        return Follow.objects.filter(follower=me, followed=user).exists()

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'email', 'status', 'photos', 'followed']
