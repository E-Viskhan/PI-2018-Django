from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
