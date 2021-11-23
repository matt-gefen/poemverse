from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class Poem(models.Model):
  title = models.CharField(max_length=150)
  author = models.CharField(max_length=100)
  linecount = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
