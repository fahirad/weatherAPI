from django.db import models

# translates db code to python format

# Create your models here.

class Weather(models.Model):
    city = models.CharField()
    temperature = models.FloatField()
    

    def __str__self():
        return self.city