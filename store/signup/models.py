from django.db import models

class Signup(models.Model):
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

class Vent(models.Model):
    problem = models.CharField(max_length=9999)
# Create your models here.
