from django.contrib import admin
from .models import Reservation

# Register your models here.
@admin.register(Reservation)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'address',  'room_number', 'check_in', 'check_out', 'amount']