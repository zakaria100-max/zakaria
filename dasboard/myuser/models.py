from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from .constants import TITLE_CHOICES, ROLE_CHOICES, SALUTATION_CHOICES
# Create your models here.


class Benutzer(models.Model):

    email = models.EmailField(('Email'), unique=True)
    first_name = models.CharField(('First Name'), max_length=64)
    last_name = models.CharField(('Last Name'), max_length=64)
    role = models.CharField(
        ('Role'), max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    is_active = models.BooleanField(('Is Active'), default=False)
    is_admin = models.BooleanField(('Is Admin'), default=False)
    is_staff = models.BooleanField(('Is Staff'), default=False)
    email_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(('Date joined'), auto_now_add=True)

    title = models.CharField(
        ('Title'), max_length=10, choices=TITLE_CHOICES, null=True, blank=True)

    no_password_set = models.BooleanField(
        ('No password set'), default=False,
        help_text=('Forces to change password on login'))




    class Meta:
        verbose_name = ('Email user')
        verbose_name_plural = ('Benutzer')
