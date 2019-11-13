from django.db import models
from categories.models import Category
from seasons.models import Season


class Serial(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    premiere_date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    seasons = models.ManyToManyField(Season)

    def __str__(self):
        return self.title
