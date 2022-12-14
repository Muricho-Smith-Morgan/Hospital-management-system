from django.contrib import admin
from .models import Hompage

# Register your models here.
@admin.register(Hompage)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['image', 'title', 'content']