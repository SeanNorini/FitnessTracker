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

def read_workout(user, workout_form) -> WorkoutLog:
    workout = WorkoutLog()
    workout.user = user
    workout.name = workout_form.cleaned_data["name"]

    exercises = workout_form.cleaned_data["exercises"].split(",")
    weights = workout_form.cleaned_data["weights"].split(",")
    reps = workout_form.cleaned_data["reps"].split(",")
    
    set_logs = {}
    for i, exercise in enumerate(exercises):
        if exercise not in set_logs:
            set_number = 1
            set_logs[exercise] = {"sets":[]}

        if weights[i] == '':
            weights[i] = 0
        if reps[i] == '':
            reps[i] = 0
        
        new_set = {"number":set_number, "weight":weights[i], "reps":reps[i]}
        set_logs[exercise]["sets"].append(new_set)

        set_number += 1
    
    workout.set_logs = set_logs

    return workout
    
