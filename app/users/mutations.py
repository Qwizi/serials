from graphene_django.forms.mutation import DjangoFormMutation
import graphene
from .forms import UserCreateForm
from .schema import UserType


class CreateUserMutation(DjangoFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = UserCreateForm


class Mutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()