from django.db import models

# Create your models here.
class Hompage(models.Model):
    image = models.ImageField(upload_to='slideshows',null=True,blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()

