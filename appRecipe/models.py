from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient')

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as per your schema requirements
