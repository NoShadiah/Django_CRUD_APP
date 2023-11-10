
# Recipes model
from django.db import models


class Recipe(models.Model):
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=False)
    added = models.DateTimeField(auto_now=True)
    updated = models.DateField(blank=True)

    def __str__(self):
        return f'{self.title} was added on {self.added}'