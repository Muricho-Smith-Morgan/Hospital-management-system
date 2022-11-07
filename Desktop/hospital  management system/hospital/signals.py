from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Doctor, Reception

@receiver(post_save, sender=User)
def connect_doctors(sender, instance, created, **kwargs):
    if created:
        Doctor.objects.create(name=instance)


@receiver(post_save, sender=User)
def connect_reception(sender, instance, created, **kwargs):
    if created:
        Reception.objects.create(rel=instance)