from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('causes', views.causes, name='causes'),
    path('event', views.event, name='event'),
    path('blog', views.blog, name='blog'),
    path('single', views.single, name='single'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('donate', views.donate, name='donate'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('contact', views.contact, name='contact'),
]