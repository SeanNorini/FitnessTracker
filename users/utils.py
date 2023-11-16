from .forms import RegistrationForm
from django.db import IntegrityError
from .models import User
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from dotenv import load_dotenv
import os

load_dotenv()

def read_registration(form):
    user_info = {}
    user_config = {}
    if form.is_valid():
          user_info["username"] = form.cleaned_data["username"]
          user_info["first_name"] = form.cleaned_data["first_name"] if form.cleaned_data["first_name"] else "Jane"
          user_info["last_name"] = form.cleaned_data["last_name"] if form.cleaned_data["last_name"] else "Doe"
          user_info["password"] = form.cleaned_data["password"]
          user_info["email"] = form.cleaned_data["email"]
          user_config["gender"] = form.cleaned_data["gender"]
          user_config["height"] = form.cleaned_data["height"] if form.cleaned_data["height"] else 70
          user_config["weight"] = form.cleaned_data["weight"] if form.cleaned_data["weight"] else 180
          user_config["age"] = form.cleaned_data["age"] if form.cleaned_data["age"] else 30
    else:
        raise ValidationError("Invalid form data.")

    if user_info["password"] == form.cleaned_data["confirm_password"]:
        return user_info, user_config
    else:
        raise ValidationError("Passwords did not match.")


def create_user(**user_contact) -> User:
    user = User.objects.create_user(**user_contact, is_staff=False)
    user.save()
    return user

def update_user_attrs(username, **user_attrs) -> None:
    pass

def send_email_confirmation(**user_info) -> None:
   
    html_body = render_to_string("users/registration-email.html", user_info)
    

    message = EmailMultiAlternatives(
       subject='Your Account is now Registered.',
       body="mail testing",
       from_email= os.environ["EMAIL_HOST_USER"],
       to=["snorini@gmail.com"]
    )
    message.attach_alternative(html_body, "text/html")
    message.send(fail_silently=False)