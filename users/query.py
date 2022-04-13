import graphene
from graphene_django import DjangoObjectType
from .models import CustomUser


class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        exclude = ('password',)


class Query(graphene.ObjectType):
    all_users = graphene.List(CustomUserType)

    def resolve_all_users(root, info):
        # We can easily optimize query count in the resolve method
        return CustomUser.objects.all()
