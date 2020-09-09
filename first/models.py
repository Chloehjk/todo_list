from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)

class Score(models.Model):
    name = models.CharField(max_length=10)
    math = models.CharField(max_length=30)
    english = models.CharField(max_length=30)
    science = models.CharField(max_length=30)