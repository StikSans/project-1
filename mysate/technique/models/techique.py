from django.db import models

class Techique(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='technique/madia/%Y/%m/%d')
    description = models.TextField()
    rating = models.IntegerField()
    price = models.IntegerField()