from django.db import models

# Create your models here.

class form_org(models.Model):
    date = models.DateField()
    Exercise = models.CharField(max_length=30)
    Meditation = models.CharField(max_length=30)
    Devotion = models.CharField(max_length=30)
    Practice = models.CharField(max_length=30)
    No_junkFood = models.CharField(max_length=30)
    Optimistic = models.CharField(max_length=30)
    Manan = models.CharField(max_length=30)
    Shoka = models.CharField(max_length=30)
    Vyartha = models.CharField(max_length=30)
    Glitch = models.CharField(max_length=30)