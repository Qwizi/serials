from django.db import models
from categories.models import Category


class Serial(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    premiere_date = models.CharField(max_length=128)
    categories = models.ManyToManyField(Category)
    #seasons = models.ManyToManyField(Season)

    def __str__(self):
        return self.title
