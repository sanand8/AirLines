from django.db import models

# Create your models here.
class Hotels(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField()
    Date = models.DateField()
    From = models.CharField(max_length=50)
    To = models.CharField(max_length=50)
    