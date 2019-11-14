from graphene_django import DjangoObjectType
import graphene
from .models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class CreateCategory(graphene.Mutation):
    category = graphene.Field(CategoryType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(self, info, name):
        category = Category()
        category.name = name
        category.save()

        return CreateCategory(category=category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, category_id=graphene.String())

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_category(self, info, category_id):
        return Category.objects.get(pk=category_id)
