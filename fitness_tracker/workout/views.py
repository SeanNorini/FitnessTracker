from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from dotenv import load_dotenv
from django.contrib.auth.decorators import login_required
import os

load_dotenv()
# Create your views here.
@login_required
def index(request):
    #user.get_module_list()
    modules = ["Workout", "Cardio", "Log", "Stats", "Settings"]
    return render(request, "workout/index.html", {"modules":modules})



@login_required
def add_exercise(request, exercise):
    if request.method == "GET":
        return render(request, "workout/exercise.html", {"exercise": exercise})
    else:
        HttpResponseRedirect(reverse("index"))

@login_required
def add_set(request):
    if request.method == "GET":
        return render(request, "workout/set.html")
    else:
        HttpResponseRedirect(reverse("index"))
        
  