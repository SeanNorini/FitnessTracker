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
    modules = ["Workout", "Cardio", "Log", "Stats", "Settings"]

    return render(request, "workout/index.html", {"modules":modules, "default_sets": range(3),
                                                  "exercises": exercises, "workouts": workouts})

@login_required
def add_exercise(request, exercise):
    if request.method == "GET":
        return render(request, "workout/exercise.html", {"exercise": exercise, "default_sets": range(3)})
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
            workout_log, exercise_sets = read_workout(request.user, workout_form)
            workout_log.save()
            for set in exercise_sets:
                set.save()
            return JsonResponse({"success":True})
        return JsonResponse({"error":"Invalid Form"})
  