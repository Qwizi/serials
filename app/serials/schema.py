from graphene_django import DjangoObjectType
import graphene
from .models import Serial


class SerialType(DjangoObjectType):
    class Meta:
        model = Serial
        fields = '__all__'


class Query(graphene.ObjectType):
    serials = graphene.List(SerialType)
    serial = graphene.Field(SerialType, serial_id=graphene.String())

    def resolve_serials(self, info):
        return Serial.objects.all()

    def resolve_serial(self, info, serial_id):
        return Serial.objects.get(pk=serial_id)
