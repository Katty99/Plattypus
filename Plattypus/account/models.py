from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import Sum
from django.contrib.auth import models as auth_models
from django.utils.safestring import mark_safe

from Plattypus.account.validators import minimum_age_validator


class PlattypusUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    Genders = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    }
    first_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
        )
    )

    last_name = models.CharField(
        max_length=30,
        validators=(
            MinLengthValidator(2),
        )
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.CharField(
        max_length=12,
        choices=Genders,
    )

    date_of_birth = models.DateField(
        validators=[minimum_age_validator]
    )

    profile_picture = models.ImageField(
        upload_to='images',
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result
