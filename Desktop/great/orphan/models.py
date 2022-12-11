from django.db import models

# Create your models here.
class Hompage(models.Model):
    image= models.ImageField(upload_to='homepage_background_images')
    title = models.CharField(max_length=100)
    content = models.TextField()

