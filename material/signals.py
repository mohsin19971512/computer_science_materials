from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student


@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    # print('sender', sender)
    if created :
        Student.objects.create(user=instance)

