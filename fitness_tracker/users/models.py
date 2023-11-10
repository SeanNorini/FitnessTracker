from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    remember_me = models.BooleanField(default=False)
    config = models.JSONField(null=True, blank=True)