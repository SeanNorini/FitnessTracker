from .models import *
from users.models import *

def save_exercise(name: str) -> Exercise:
    exercise = Exercise()
    exercise.name = name
    exercise.save()
    return exercise
    

def save_workout(exercises: list) -> Workout:
    workout = Workout()
    workout.exercises.set(exercises)
    workout.save()
    return workout

def save_current_workout(exercise_logs: list) -> Workout:
    workout = WorkoutLog()
    workout.exercises.set(exercise_logs)
    workout.save()
    return workout

def delete_record(obj: object) -> None:
    obj.delete()

def read_workout(user, workout_form) -> [WorkoutLog, [ExerciseSet]]:
    workout = WorkoutLog()
    workout.user = user
    workout.name = workout_form.cleaned_data["name"]

    exercises = workout_form.cleaned_data["exercises"].split(",")
    weights = workout_form.cleaned_data["weights"].split(",")
    reps = workout_form.cleaned_data["reps"].split(",")
    
    sets = []
    for i in range(len(weights)):
        if weights[i] == '':
            weights[i] = 0
        if reps[i] == '':
            reps[i] = 0
        exercise = Exercise.objects.get(name=exercises[i])
        
        new_set = ExerciseSet(workout_log=workout, exercise=exercise, weight=weights[i], reps=reps[i])
        sets.append(new_set)
    
    return workout, sets
    
