from django.db import models
from django.utils import timezone

# Create your models here.
class Weight(models.Model):
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    date = models.DateField(default=timezone.now)
    bmi = models.FloatField(default=0)
    himendo = ''
    def bmi_check(self):
        if self.bmi < 18.5:
            himando = '痩せ型'
        elif (self.bmi >= 18.5) and (self.bmi < 25):
            himando = '標準体型'
        elif (self.bmi >= 25) and (self.bmi < 30):
            himando = '肥満(軽)'
        else:
            himando = '肥満(重)'
        return himando