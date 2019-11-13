from graphene_django import DjangoObjectType
import graphene
from .models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class Query(graphene.ObjectType):
    categories = graphene.List(CategoryType)
    category = graphene.Field(CategoryType, category_id=graphene.String())

    def resolve_categories(self, info):
        return Category.objects.all()

    def resolve_category(self, info, category_id):
        return Category.objects.get(pk=category_id)


schema = graphene.Schema(query=Query)
