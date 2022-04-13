import graphene
from users.query import Query as UsersQuery
from follows.query import Query as FollowsQuery
from posts.query import Query as PostsQuery
from profiles.query import Query as ProfileQuery


class Query(FollowsQuery, PostsQuery, UsersQuery, ProfileQuery):
    pass


schema = graphene.Schema(query=Query)
