from django.db.models.signals import post_save
from django.dispatch import receiver

from register.models import Profile, BlogUser


@receiver(post_save, sender=BlogUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
