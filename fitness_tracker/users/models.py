from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    remember_me = models.BooleanField(default=False)


class UserAttributes(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.FloatField(default=180)
    weight = models.FloatField(default=70)
    age = models.IntegerField(default=30)

    def update_attrs(self, username, height, weight, age):
        self.user_id = User.objects.get(username=username)
        self.height = height
        self.weight = weight
        self.age = age
        