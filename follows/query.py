import graphene
from graphene_django import DjangoObjectType
from .models import Follow


class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
        fields = "__all__"


class Query(graphene.ObjectType):
    all_follows = graphene.List(FollowType)

    def resolve_all_follows(root, info):
        # We can easily optimize query count in the resolve method
        return Follow.objects.all()
