from django.db import models

# Create your models here.
class Diet(models.Model):
    users = models.CharField(max_length=50, null=True)
    age  = models.IntegerField(max_length=50, null=True)
    height = models.IntegerField(max_length=50, null=True)
    weight = models.IntegerField(max_length=50, null=True)
    gender = models.CharField(max_length=50, null=True)
    activity = models.CharField(max_length=50, null=True)
    diabetes = models.CharField(max_length=50, null=True)
    heart = models.CharField(max_length=50, null=True)
    kidney = models.CharField(max_length=50, null=True)
    
    


class BodyMassIndex(models.Model):
    BMI = models.CharField(max_length=50,null=True)

class Calories(models.Model):
    defg = models.CharField(max_length=50,null=True)
