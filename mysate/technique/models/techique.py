from django.db import models

class Techique(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    price = models.IntegerField()