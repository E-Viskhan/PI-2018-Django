from datetime import timedelta

from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.settings import MAX_COUNT_POSTS
from posts.models import Post
from posts.serializers import PostSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        last = timezone.now() - timedelta(hours=24)
        posts = Post.objects.filter(created_at__gte=last)
        if posts.count() > MAX_COUNT_POSTS:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
