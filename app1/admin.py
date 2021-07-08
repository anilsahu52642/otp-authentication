from django.contrib import admin
from .models import customuser
# Register your models here.


@admin.register(customuser)
class customuserAdmin(admin.ModelAdmin):
    list_display = ['mobile','otp']