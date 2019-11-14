from graphene_django import DjangoObjectType
import graphene
from .models import Season
from serials.models import Serial


class SeasonType(DjangoObjectType):
    class Meta:
        model = Season


class SeasonInput(graphene.InputObjectType):
    id = graphene.ID()
    serial = graphene.ID()
    number = graphene.Int()


class CreateSerialSeason(graphene.Mutation):
    class Arguments:
        input = SeasonInput(required=True)

    season = graphene.Field(SeasonType)

    def mutate(self, info, input):
        serial_instance = Serial.objects.get(pk=input.serial)
        if serial_instance is None:
            return CreateSerialSeason(season=None)
        season_instance = Season.objects.create(
            serial=serial_instance,
            number=input.number
        )

        return CreateSerialSeason(season=season_instance)


class Mutation(graphene.ObjectType):
    create_serial_season = CreateSerialSeason.Field()


class Query(graphene.ObjectType):
    seasons = graphene.List(SeasonType)
    season = graphene.Field(SeasonType, season_id=graphene.String())

    def resolve_seasons(self, info):
        return Season.objects.all()

    def resolve_season(self, info, season_id):
        return Season.objects.get(pk=season_id)
