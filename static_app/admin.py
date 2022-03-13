from django.contrib import admin
from django.contrib.admin import ModelAdmin
from static_app.models import *

# Register your models here.

@admin.register(Stats)
class Statistica_admin(ModelAdmin):
    pass