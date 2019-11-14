from django.db import models
from seasons.models import Season


class Episode(models.Model):
    title = models.CharField(max_length=64)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, default=1)
