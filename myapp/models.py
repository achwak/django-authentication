from __future__ import unicode_literals
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
