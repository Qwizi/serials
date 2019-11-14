from graphene_django import DjangoObjectType
import graphene
from .models import Episode
from seasons.models import Season


class EpisodeType(DjangoObjectType):
    class Meta:
        model = Episode


class EpisodeInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    season = graphene.ID()


class CreateSerialSeasonEpisode(graphene.Mutation):
    class Arguments:
        input = EpisodeInput(required=True)

    episode = graphene.Field(EpisodeType)

    def mutate(self, info, input):
        season_instance = Season.objects.get(pk=input.season)
        if season_instance is None:
            return CreateSerialSeasonEpisode(episode=None)
        episode_instance = Episode.objects.create(
            title=input.title,
            season=season_instance
        )
        return CreateSerialSeasonEpisode(episode=episode_instance)


class Mutation(graphene.ObjectType):
    create_serial_season_episode = CreateSerialSeasonEpisode.Field()


class Query(graphene.ObjectType):
    episodes = graphene.List(EpisodeType)
    episode = graphene.Field(EpisodeType, episode_id=graphene.String())

    def resolve_episodes(self, info):
        return Episode.objects.all()

    def resovle_episode(self, info, episode_id):
        return Episode.objects.get(pk=episode_id)
