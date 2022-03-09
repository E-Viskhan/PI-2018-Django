from rest_framework import serializers

from follows.models import Follow


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follow
        fields = '__all__'