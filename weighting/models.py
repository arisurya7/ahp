from django.db import models

# Create your models here.
class Responden(models.Model):
    id_responden = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    birth_date = models.DateField(default=None, blank=True, null=True)
    gender = models.CharField(max_length=10)
    name_company = models.CharField(max_length=100)
    businness_field = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    experience = models.CharField(max_length=50)

class WeightRFM(models.Model):
    id = models.AutoField(primary_key=True)
    id_responden = models.IntegerField()
    w_recency = models.FloatField()
    w_frequency = models.FloatField()
    w_monetary = models.FloatField()
    score_input = models.TextField(default=None, blank=True, null=True)

class WeightLRFM(models.Model):
    id = models.AutoField(primary_key=True)
    id_responden = models.IntegerField()
    w_length = models.FloatField()
    w_recency = models.FloatField()
    w_frequency = models.FloatField()
    w_monetary = models.FloatField()
    score_input = models.TextField(default=None, blank=True, null=True)

