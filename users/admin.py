from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ["config"]}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ["config"]}),)

# Register your models here.
admin.site.register(User, CustomUserAdmin)
