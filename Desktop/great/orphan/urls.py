from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('causes', views.causes, name='causes'),
    path('event', views.event, name='event'),
    path('blog', views.blog, name='blog'),
]