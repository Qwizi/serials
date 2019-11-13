from django.db import models
from episodes.models import Episode


class Season(models.Model):
    number = models.IntegerField()
    episodes = models.ManyToManyField(Episode)

    def create_season_name(self):
        return 'Sezon - {}'.format(self.number)

    def __str__(self):
        return self.number
