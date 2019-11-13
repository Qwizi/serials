from graphene_django import DjangoObjectType
import graphene
from .models import Season


class SeasonType(DjangoObjectType):
    class Meta:
        model = Season


class Query(graphene.ObjectType):
    seasons = graphene.List(SeasonType)
    season = graphene.Field(SeasonType, season_id=graphene.String())

    def resolve_seasons(self, info):
        return Season.objects.all()

    def resolve_season(self, info, season_id):
        return Season.objects.get(pk=season_id)