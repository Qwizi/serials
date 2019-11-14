from django.db import models
from serials.models import Serial


class Season(models.Model):
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE, default=1)
    number = models.IntegerField()

    def create_season_name(self):
        return 'Sezon - {}'.format(self.number)

    def __str__(self):
        return self.number
