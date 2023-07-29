from django.db import models

from Plattypus.account.validators import minimum_age_validator, email_validator


# Create your models here.
class Account(models.Model):
    NAMES_MAX_LENGTH = 30
    first_name = models.CharField(max_length=NAMES_MAX_LENGTH)
    last_name = models.CharField(max_length=NAMES_MAX_LENGTH)
    email_address = models.CharField(max_length=254, validators=[email_validator])
    password = models.CharField(max_length=30)
    birthday = models.DateField(validators=[minimum_age_validator])
    profile_picture = models.ImageField(blank=True, null=True)
