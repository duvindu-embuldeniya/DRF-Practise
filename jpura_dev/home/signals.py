from django.db.models.signals import post_save, post_delete
from . models import Profile
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail

from django.conf import settings


@receiver(post_save, sender = User)
def createProfile(sender, instance, created, *args, **kwargs):
    if created:
        created_user = instance
        Profile.objects.create(
            user = created_user
        )

    username = instance.username

    subject = f"Welcome {username}"
    message = 'Thanks for contacting us! We\'ll get back in you soon!'
    sender = settings.EMAIL_HOST_USER
    recipient_mail = instance.email

    send_mail(
        subject,
        message,
        sender,
        [recipient_mail],
        fail_silently = False,
    )




@receiver(post_delete, sender = Profile)
def deleteUser(sender, instance, *args, **kwargs):
    instance.user.delete()



# post_save.connect(createProfile, sender=User)
# post_delete.connect(deleteUser, sender=Profile)