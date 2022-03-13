from django.contrib import admin
from django.contrib.admin import ModelAdmin
from main_app.models import *

# Register your models here.

@admin.register(Ombor)
class Ombor_admin(ModelAdmin):
    pass

@admin.register(Product)
class Product_admin(ModelAdmin):
    pass

@admin.register(Client)
class Client_admin(ModelAdmin):
    pass