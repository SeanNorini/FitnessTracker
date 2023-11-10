from django.db import models
from users.models import User
from datetime import date

# Create your models here.
class Exercise(models.Model):
    def exercise_default():
        return {"sets":[{"number": 1, "weight":0, "reps":8},{"number": 2, "weight":0, "reps":8},{"number": 3, "weight":0, "reps":8}]}
    name = models.CharField(primary_key="True", max_length=50)
    config = models.JSONField(default=exercise_default)

class Workout(models.Model):
    name = models.CharField(primary_key="True", max_length=50)
    config = models.JSONField(null=True, blank=True)

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())
    set_logs = models.JSONField()





