from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    born_date = models.DateField()
    height = models.IntegerField()