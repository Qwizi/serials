from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoFormMutation
import graphene
from .models import Serial
from .forms import SerialForm
from categories.models import Category
from categories.schema import CategoryInput


class SerialType(DjangoObjectType):
    class Meta:
        model = Serial


class SerialInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    premiereDate = graphene.String()
    categories = graphene.List(CategoryInput)


class CreateSerial(graphene.Mutation):
    class Arguments:
        input = SerialInput(required=True)

    serial = graphene.Field(SerialType)

    def mutate(self, info, input=None):
        categories = []
        for category_input in input.categories:
            category = Category.objects.get(pk=category_input.id)
            if category is None:
                return CreateSerial(serial=None)
            categories.append(category)
        serial_instance = Serial(
            title=input.title,
            description=input.description,
            premiere_date=input.premiereDate
        )
        serial_instance.save()
        serial_instance.categories.set(categories)
        return CreateSerial(serial=serial_instance)


class Mutation(graphene.ObjectType):
    create_serial = CreateSerial.Field()


class Query(graphene.ObjectType):
    serials = graphene.List(SerialType)
    serial = graphene.Field(SerialType, serial_id=graphene.String())

    def resolve_serials(self, info):
        return Serial.objects.all()

    def resolve_serial(self, info, serial_id):
        return Serial.objects.get(pk=serial_id)
