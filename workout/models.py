from django.db import models
from users.models import User
from datetime import date

# Create your models here.
class BaseExercise(models.Model):
    def default_sets():
        return {"sets":[{"number": 1, "weight":0, "reps":8},{"number": 2, "weight":0, "reps":8},{"number": 3, "weight":0, "reps":8}]}
    
    name = models.CharField(primary_key="True", max_length=50)
    sets = models.JSONField(default=default_sets)

    class Meta:
        abstract = True


class Exercise(BaseExercise):
    pass


class CustomExercise(BaseExercise):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class BaseWorkout(models.Model):
    name = models.CharField(primary_key="True", max_length=50)
    config = models.JSONField(null=True, blank=True)

    class Meta:
        abstract = True


class Workout(BaseWorkout):
    pass


class CustomWorkout(BaseWorkout):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    date = models.DateField(default=date.today())


class ExerciseLog(BaseExercise):
    workout_log = models.ForeignKey(WorkoutLog, on_delete=models.CASCADE)

