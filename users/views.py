from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import LoginForm, RegistrationForm, SettingsForm
from .utils import read_registration, create_user, update_user_attrs, send_email_confirmation
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .models import User
import json

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
 
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            remember_me = login_form.cleaned_data["remember_me"]
        else:
            return render(request, "users/login.html", {"form":LoginForm()})

        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
                user.remember_me = False
                user.save()
            return HttpResponseRedirect(reverse("index"))
        else:    
            return render(request, "users/login.html", {"form":LoginForm(), 
                          "message": "Invalid username and/or password."})

    return render(request, "users/login.html", {"form":LoginForm()})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return HttpResponseRedirect(reverse("index"))

def registration(request):
    # Check for form data
    if request.method=="POST":  
        try:
            # Read data into contact info and physical attributes
            form = RegistrationForm(request.POST) 
            user_info, user_config = read_registration(form)
            
        except ValidationError as error:
            # If form isn't valid or password doesn't match, return error message.
            return JsonResponse({"message": str(error)})

        # Attempt to create a new user, update their info and log in to main page. 
        try:
            user = create_user(config=user_config, **user_info)
            send_email_confirmation(**user_info)
            login(request, user)
            return JsonResponse({"success":True})
        except IntegrityError:
            return JsonResponse({"message":"Username already taken."})
            

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/registration.html", {"form": RegistrationForm()})
  
@login_required
def user_settings(request):
    user = request.user
    if request.method == "POST":
        form = SettingsForm(request.POST)  
        if form.is_valid():  
            user.first_name = form.cleaned_data["first_name"]
            user.first_name = form.cleaned_data["last_name"]
            user.first_name = form.cleaned_data["email"]
            gender = form.cleaned_data["gender"]
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            age = form.cleaned_data["age"]
            user.config = {"gender":gender,"height":height, 
                      "weight":weight, "age":age}
            user.save()
            return JsonResponse({"success":True})
    #user.get_module_list()
    modules = ["workout", "cardio", "log", "stats", "settings"]
    form = SettingsForm()
    for field_name, field in form.fields.items():
        config = user.config
        if field_name in ["gender", "height", "weight", "age"]:
            field.widget.attrs["value"] = config[field_name]
        else:
            field.widget.attrs["value"] = getattr(user, field_name)
    return render(request, "users/settings.html", {"modules": modules, "form": form})
          
        
    