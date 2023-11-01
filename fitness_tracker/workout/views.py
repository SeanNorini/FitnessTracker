from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

# Create your views here.
def index(request):
    
    send_mail(
        "Test",
        "Test",
        "Test@example.com",
        ["snorini@gmail.com"],
        fail_silently=False,
    )

    if request.user.is_authenticated:
        #user.get_module_list()
        modules = ["Workout", "Cardio", "Log", "Stats", "Settings"]
        return render(request, "workout/index.html", {"modules":modules})
    else:
        return HttpResponseRedirect(reverse("login"))
  