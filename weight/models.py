from django.db import models
from django.utils import timezone

# Create your models here.
class Weight(models.Model):
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    date = models.DateField(default=timezone.now)