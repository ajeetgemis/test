from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

@receiver(post_save,sender=User)
def send_email_signal(sender,instance,created,**kwargs):
    if created and instance.email:
        message='hdbfvjhsbfjshk'
        subject='dsdvsd'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
          #  fail_silently=False,
        )
        print(instance.email)
        print("signal called")
