import graphene
import users.schema
import categories.schema
import serials.schema
import seasons.schema
import episodes.schema


# from users.mutations import Mutation as UserMutation


class Query(
    users.schema.Query,
    categories.schema.Query,
    serials.schema.Query,
    seasons.schema.Query,
    episodes.schema.Query,
    graphene.ObjectType
):
    pass


class Mutation(
    categories.schema.Mutation,
    serials.schema.Mutation,
    seasons.schema.Mutation,
    episodes.schema.Mutation,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
