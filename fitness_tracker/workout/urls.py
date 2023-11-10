from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("add_exercise/<str:exercise>", views.add_exercise, name="add_exercise"),
  path("add_set", views.add_set, name="add_set"),
  path("save_workout", views.save_workout, name="save_workout"),
  path("select_workout/<str:workout_name>", views.select_workout, name="select_workout"),
  path("edit_workout", views.edit_workout, name="edit_workout"),
]