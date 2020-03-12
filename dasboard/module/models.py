from django.db import models

from .constants import (
 LEGAL_CHOICES,
  TITLE_CHOICES,
  Stufen,
  SALUTATION_CHOICES,
  TITLE_CHOICES,
  )
from django_countries.fields import CountryField


# Create your models here.
class Module(models.Model):

    module_id = models.CharField(
        ('Module ID'), max_length=64, unique=True, null=True)
    module = models.CharField(('Modulname'), max_length=128)
    module_wahl = models.CharField(
        ('Fach'), max_length=100, choices=LEGAL_CHOICES, blank=True)
    martikelnummer= models.IntegerField( blank=True)
    international_prefix = CountryField(
        null=True, blank=True, verbose_name=('International prefix'))
    phone_number = models.CharField(
        ('Telephone Nr'), max_length=20, null=True, blank=True)
    email= models.EmailField(('Email'), unique=True)


    class Meta:
        verbose_name = ('Module')
        verbose_name_plural = ('Module')

    def __str__(self):
        return self.module



class Owner(models.Model):

    owner_id = models.CharField(
        ('Studenten_ID'), max_length=64, unique=True, null=True)
    is_student = models.BooleanField(('is_student'), null=True)
    studienstufe= models.CharField(
        ('Stufen'), max_length=16,
        choices=Stufen)

    salutation = models.CharField(
        ('Salutation'), null=True, blank=True, max_length=4,
        choices=SALUTATION_CHOICES)
    title = models.CharField(
        ('Title'), max_length=10, choices=TITLE_CHOICES, null=True, blank=True)
    first_name = models.CharField(('First Name'), max_length=64)
    last_name = models.CharField(('Last Name'), max_length=64)
    email = models.EmailField(('Email'), null=True, blank=True)
    birthday = models.DateField(('Birthday'), null=True, blank=True)
    private_address_street = models.CharField(
        ('Street of Private Address'), max_length=50, blank=True)
    private_address_house_n = models.CharField(
        ('House Number of Private Address'), max_length=10, blank=True)
    private_address_extra = models.CharField(
        ('Addition to Address'), max_length=50, blank=True)
    private_address_postcode = models.CharField(
        ('Postcode of Private Address'), max_length=6, blank=True)
    private_address_city = models.CharField(
        ('City of Private Address'), max_length=50, blank=True)
    telephone = models.CharField(
        ('Telephone Nr'), max_length=20, null=True, blank=True)
    student_profile = models.ForeignKey(
        Module, on_delete=models.CASCADE,
        verbose_name=('Module'), blank=True, null=True,
        related_name='owners')

    class Meta:
        verbose_name = ('Student')
        verbose_name_plural = ('Student')
        ordering = ('-is_student', 'last_name', 'id',)
