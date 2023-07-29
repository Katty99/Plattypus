from django.core.exceptions import ValidationError


def minimum_income(amount):
    if amount < 10:
        raise ValidationError("Income must be at least 10.")