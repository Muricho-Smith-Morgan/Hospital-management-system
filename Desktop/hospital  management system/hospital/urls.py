
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('About/', views.About, name='About'),
    path('Contact', views.Contact, name='Contact'),
    path('Doctor', views.Doctor, name='Doctor'),
    path('Receptionist', views.Receptionist, name='Receptionist'),
    path('reception', views.reception, name = 'reception'),
    path('Doctor_panel', views.Doctor_panel, name = 'Doctor_panel'),
    path('Reception_panel', views.Reception_panel, name = 'Reception_panel'),
    path('Add_patient', views.Add_patient, name = 'Add_patient'),
    path('View_patient', views.View_patient, name = 'View_patient'),
    path('Emergency', views.Emergency, name = 'Emergency'),
    path('edit-patient-info/<str:pk>/', views.edit_patient_info, name='edit_patient'),
    path('delete-patient-info/<str:pk>/', views.delete_patient_info, name='delete_patient'),
    path('edit-patient-status/<str:pk>/', views.edit_patient_status, name='edit_status'),
    path('appointment', views.appointment, name='appointment'),
]
