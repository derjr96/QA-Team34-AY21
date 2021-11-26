from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# using these Decorators to create a profile image with the default.jpg when creating an account
@receiver(post_save, sender=User)  # when a user is saved, send a post_save signal
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)  # when a user is saved, send a post_save signal
def save_profile(sender, instance, **kwargs):
    instance.profile.save()