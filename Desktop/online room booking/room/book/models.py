from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    room_number = models.CharField(max_length=50)
    check_in = models.CharField(max_length=30)
    check_out = models.CharField(max_length=30)
    amount = models.CharField(max_length=20)
    status = models.CharField(max_length=50, default='')
   
    
   
    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.name,self.id)