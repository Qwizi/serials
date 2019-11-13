from graphene_django import DjangoObjectType
import graphene
from .models import User as UserModel


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        exclude = ('password',)


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(UserType, user_id=graphene.String())

    def resolve_users(self, info):
        return UserModel.objects.all()


schema = graphene.Schema(query=Query)
