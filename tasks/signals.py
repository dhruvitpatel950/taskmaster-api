from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Task
from .tasks import send_welcome_email

@receiver(post_save, sender=Task)
def update_project_timestamp(sender, instance, created, **kwrgs):
    if instance.project:
        instance.project.save()
        print(f"Signal Fired: Updated timestamp for Project '{instance.project.name}'")

@receiver(post_save, sender=Task)
def task_created_alert(sender, instance, created, **kwargs):
    if created:
        # Instead of calling send_welcome_email(user), we call .delay(user)
        # This sends it to Redis. Django continues immediately.
        send_welcome_email.delay(instance.owner.username)
        print("Task queued for background worker!")
