from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
from .utils import *
from .models import *
from .forms import WorkoutForm
import os

load_dotenv()
# Create your views here.
@login_required
def index(request):
    custom_exercises = list(CustomExercise.objects.filter(user=request.user).values_list("name", flat=True))
    custom_workouts = list(CustomWorkout.objects.filter(user=request.user).values_list("name", flat=True))
    custom_exercises.extend(list(Exercise.objects.exclude(name__in=custom_exercises).values_list("name", flat=True)))
    custom_workouts.extend(list(Workout.objects.exclude(name__in=custom_workouts).values_list("name", flat=True)))


    #user.get_module_list()
    modules = ["workout", "cardio", "log", "stats", "settings"]

    return render(request, "workout/index.html", {"modules":modules,
                                                  "exercises": custom_exercises, "workouts": custom_workouts})

@login_required
def add_exercise(request, exercise):
    if (CustomExercise.objects.filter(user=request.user).exists()):
        exercise = CustomExercise.objects.get(name=exercise.replace('%20', ' '))    
    else:
        exercise = Exercise.objects.get(name=exercise.replace('%20', ' '))
    sets = exercise.sets
    return render(request, "workout/exercise.html", {"exercise": exercise.name, "sets": sets})


@login_required
def add_set(request):
    return render(request, "workout/set.html")
    
    
@login_required
def save_workout_session(request):
    if request.method == "POST":
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout_log = read_workout_session(request.user, workout_form)
            workout_log.save()
            
            return JsonResponse({"success":True})
        return JsonResponse({"error":"Invalid Form"})
    
@login_required
def save_workout(request):
    if request.method == "POST":
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            custom_workout = read_workout(request.user, workout_form)
            custom_workout.save()
            
            return JsonResponse({"success":True})
        return JsonResponse({"error":"Invalid Form"})
    
@login_required
def select_workout(request, workout_name):
    if CustomWorkout.objects.filter(user=request.user, name=workout_name):
      workout = CustomWorkout.objects.get(name=workout_name)
    else:
      workout = Workout.objects.get(name=workout_name.replace('%20', ' '))
    return render(request, "workout/workout.html", {"workout": workout.config["exercises"]})

@login_required
def edit_workouts(request):
    custom_exercises = list(CustomExercise.objects.filter(user=request.user).values_list("name", flat=True))
    custom_workouts = list(CustomWorkout.objects.filter(user=request.user).values_list("name", flat=True))
    custom_exercises.extend(list(Exercise.objects.exclude(name__in=custom_exercises).values_list("name", flat=True)))
    custom_workouts.extend(list(Workout.objects.exclude(name__in=custom_workouts).values_list("name", flat=True)))

    return render(request, "workout/edit_workouts.html", {"workouts": custom_workouts, "exercises": custom_exercises})
  