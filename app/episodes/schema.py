from graphene_django import DjangoObjectType
import graphene
from .models import Episode


class EpisodeType(DjangoObjectType):
    class Meta:
        model = Episode


class Query(graphene.ObjectType):
    episodes = graphene.List(EpisodeType)
    episode = graphene.Field(EpisodeType, episode_id=graphene.String())

    def resolve_episodes(self, info):
        return Episode.objects.all()

    def resovle_episode(self, info, episode_id):
        return Episode.objects.get(pk=episode_id)
