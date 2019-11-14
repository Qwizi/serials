from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoModelFormMutation
import graphene
from .models import Category
from .forms import CategoryForm


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class CreateCategory(graphene.Mutation):
    class Arguments:
        input = CategoryInput(required=True)

    category = graphene.Field(CategoryType)

    def mutate(self, info, input):
        category_instance = Category.objects.create(name=input.name)

        return CreateCategory(category=category_instance)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, category_id=graphene.String())

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_category(self, info, category_id):
        return Category.objects.get(pk=category_id)
