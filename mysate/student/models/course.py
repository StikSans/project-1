from django.db import models


class Course(models.Model):
  name = models.CharField(max_length=100)
  start_date = models.DateField()
  student = models.ManyToManyField('Student')