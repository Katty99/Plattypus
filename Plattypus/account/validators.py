from datetime import date

from django.core.exceptions import ValidationError
import re


def minimum_age_validator(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age < 18:
        raise ValidationError('Must be at least 18 years old to register')


def email_validator(address):
    pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    valid_email = re.match(pattern, address)
    if not valid_email:
        raise ValidationError("The email address must be valid.")
