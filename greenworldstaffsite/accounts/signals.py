import django.dispatch
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Staff

admin_added_user = django.dispatch.Signal()

@receiver(post_save, sender=User)
def user_added_in_admin_page(sender,instance, created, **kwargs):
    full_name=instance.first_name+" "+instance.last_name
    department = instance.groups.first().name if instance.groups.exists() else "Unknown"
    staff, created = Staff.objects.get_or_create(email=instance.email)
    staff.full_name = full_name
    staff.department = department
    staff.save()