from django.db import models

class DateCalculator(models.Model):
    total_hours = models.IntegerField()
    years = models.IntegerField()
    months = models.IntegerField()
    days = models.IntegerField()
