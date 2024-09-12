from django.db import models

# Create your models here.
class Author(models.Model):
  name= models.CharField(max_length=100)
  date_of_birth = models.DateField(auto_now_add=True)
  gender = models.CharField(max_length=2)