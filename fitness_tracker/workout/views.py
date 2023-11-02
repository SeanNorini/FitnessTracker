from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from dotenv import load_dotenv
import os

load_dotenv()
# Create your views here.
def index(request):

    if request.user.is_authenticated:
        #user.get_module_list()
        modules = ["Workout", "Cardio", "Log", "Stats", "Settings"]
        return render(request, "workout/index.html", {"modules":modules})
    else:
        return HttpResponseRedirect(reverse("login"))
  