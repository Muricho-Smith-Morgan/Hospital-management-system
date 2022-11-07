from django.contrib import admin
from .models import Doctor, Reception, Patient
from django.contrib.admin.models import LogEntry

# Register your models here.
@admin.register(Doctor)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'gender', 'country', 'address', 'speciality']

@admin.register(Reception)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['rel', 'phone_number', 'gender', 'country', 'address',]


@admin.register(Patient)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'phone_number', 'residence', 'national_id']


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierachy = 'action_time'

    list_filter = ('user', 'content_type', 'action_flag')
    search_field = [
        'object_repr'
        'change_message'
    ]
    list_display = ('action_time', 'user', 'content_type', 'action_flag')