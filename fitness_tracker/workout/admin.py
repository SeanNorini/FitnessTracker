from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ExerciseSet)
admin.site.register(Exercise)
admin.site.register(ExerciseConf)
admin.site.register(Workout)

class ExerciseSetInline(admin.TabularInline):
    model = ExerciseSet

@admin.register(WorkoutLog)
class WorkoutLogAdmin(admin.ModelAdmin):
    inlines = [ExerciseSetInline]
