from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(unique=True, max_length=225)
    password = models.CharField(max_length = 128)
    last_verification_email_sent = models.DateTimeField(default=None, null=True)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    ROLE_CHOICES = [
        ('customer', ' Customer'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=25, choices=ROLE_CHOICES, null=True)
    role_set_once = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='restuarant_user_set', blank = True)
    user_permissions = models.ManyToManyField(Permission, related_name='restuarant_user_permissions', blank=True)
    
