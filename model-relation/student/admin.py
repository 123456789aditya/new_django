from django.contrib import admin

# Register your models here.
from .models import Aadhar,Citizen

@admin.register(Aadhar)
class AadharAdmin(admin.ModelAdmin):
    