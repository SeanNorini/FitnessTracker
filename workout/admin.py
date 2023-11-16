from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Exercise)
admin.site.register(CustomExercise)
admin.site.register(Workout)
admin.site.register(CustomWorkout)


class ExerciseLogInline(admin.TabularInline):
    model = ExerciseLog
    extra = 1

@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    inlines = [ExerciseLogInline]