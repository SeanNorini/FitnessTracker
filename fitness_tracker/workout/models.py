from django.db import models
from users.models import User
from datetime import date

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(primary_key="True", max_length=50)

class Workout(models.Model):
    name = models.CharField(primary_key="True", max_length=50)
    exercises = models.ManyToManyField(Exercise, blank=True)

class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today())

class ExerciseSet(models.Model):
    workout_log = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.FloatField(default=0)
    reps = models.IntegerField(default=0)

class ExerciseConf(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_name = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    default_reps = models.IntegerField(default=5)
    default_weight = models.FloatField(default=100)
    default_set_number = models.IntegerField(default=3)
    max_weight = models.FloatField(default=0)






