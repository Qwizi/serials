from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=64)