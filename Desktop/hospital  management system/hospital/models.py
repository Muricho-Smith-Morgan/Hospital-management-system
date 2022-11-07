from django.db import models 
from django.contrib.auth.models import User
from PIL import Image

# Create your models here
class Doctor(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    phone_number= models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    speciality = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    dp = models.ImageField(upload_to='Doctors/', default='default.png')

    def save(self, *args, **kwargs):
        super(Doctor, self).save(*args, **kwargs)

        pic = Image.open(self.dp.path)

        if pic.height > 400 and pic.width > 400:
            output_size = (400, 400)
            pic.thumbnail(output_size)
            pic.save(self.dp.path)

    def __str__(self):
        return f'{self.name}'

class Reception(models.Model):
    rel = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    dp = models.ImageField(upload_to='Reception/', default='default.png')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Reception, self).save(*args, **kwargs)

        pic = Image.open(self.dp.path)

        if pic.height > 400 and pic.width > 400:
            output_size = (400, 400)
            pic.thumbnail(output_size)
            pic.save(self.dp.path)

    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.first_name,self.id)

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    residence = models.CharField(max_length=50)
    national_id = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    symptoms= models.CharField(max_length=100, default='') 
    disease= models.CharField(max_length=30, default='')
    status = models.CharField(max_length=30, default='')
    
    def __str__(self):
        return 'Name: {},Id: {}'.format(self.first_name,self.id)


