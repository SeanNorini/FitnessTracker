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
    exercises = Exercise.objects.all()
    workouts = Workout.objects.all()
    #user.get_module_list()
    modules = ["workout", "cardio", "log", "stats", "settings"]

    return render(request, "workout/index.html", {"modules":modules,
                                                  "exercises": exercises, "workouts": workouts})

@login_required
def add_exercise(request, exercise):
    if request.method == "GET":
        exercise = Exercise.objects.get(name=exercise.replace('%20', ' '))
        sets = exercise.config
        return render(request, "workout/exercise.html", {"exercise": exercise.name, "sets": sets})
    else:
        HttpResponseRedirect(reverse("index"))

@login_required
def add_set(request):
    if request.method == "GET":
        return render(request, "workout/set.html")
    else:
        HttpResponseRedirect(reverse("index"))
    
@login_required
def save_workout(request):
    if request.method == "POST":
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout_log = read_workout(request.user, workout_form)
            workout_log.save()
            
            return JsonResponse({"success":True})
        return JsonResponse({"error":"Invalid Form"})
    
@login_required
def select_workout(request, workout_name):
    workout = Workout.objects.get(name=workout_name.replace('%20', ' '))
    exercises = workout.config
    
    return render(request, "workout/workout.html", {"exercises": exercises})

@login_required
def workout_settings(request):
    exercises = Exercise.objects.all()
    workouts = Workout.objects.all()
    return render(request, "workout/workout_settings.html", {"workouts": workouts, "exercises": exercises})
  