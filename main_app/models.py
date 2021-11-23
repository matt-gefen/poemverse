from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Poem(models.Model):
  title = models.CharField(max_length=150)
  author = models.CharField(max_length=100)
  lines = ArrayField(models.CharField(max_length=200))
  linecount = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
