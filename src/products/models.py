from django.db import models


# Django Models Unleashed 
# cfe.sh/projects/django-models-unleashed-2021

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()