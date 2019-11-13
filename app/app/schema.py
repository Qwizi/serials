import graphene
from users.schema import Query as UserQuery
from categories.schema import Query as CategoryQuery
from serials.schema import Query as SerialQuery
from seasons.schema import Query as SeasonQuery
from episodes.schema import Query as EpisodeQuery


# from users.mutations import Mutation as UserMutation


class Query(
    UserQuery,
    CategoryQuery,
    SerialQuery,
    SeasonQuery,
    EpisodeQuery,
    graphene.ObjectType
):
    pass


# class Mutation(
#     # UserMutation,
#     graphene.ObjectType
# ):
#     pass


schema = graphene.Schema(query=Query)
