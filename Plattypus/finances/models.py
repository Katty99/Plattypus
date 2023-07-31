from django.contrib.auth import get_user_model
from django.db import models

from Plattypus.account.models import PlattypusUser
from Plattypus.finances.validators import minimum_income

UserModel = get_user_model()

CURRENCIES = [
    ("BGN", "BGN"),
    ("GBP", "GBP"),
    ("EUR", "EUR"),
    ("USD", "USD"),
    ("CHF", "CHF"),
    ("CAD", "CAD"),
    ("AUD", "AUD"),
    ("INR", "INR"),
    ("JPY", "JPY"),
]


class Income(models.Model):
    INCOME_SOURCES = [
        ("Work", "Work"),
        ("Gift", "Gift"),
        ("Loan", "Loan"),
        ("Savings", "Savings"),
        ("Donation", "Donation"),
    ]
    amount = models.FloatField()
    currency = models.CharField(choices=CURRENCIES)
    date = models.DateField()
    source = models.CharField(choices=INCOME_SOURCES)
    details = models.CharField(blank=True, null=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result


class Expense(models.Model):
    EXPENSE_CHOICES = [
        ("Household", "Household"),
        ("Transport", "Transport"),
        ("Food", "Food"),
        ("Utilities", "Utilities"),
        ("Clothing", "Clothing"),
        ("Skincare", "Skincare"),
        ("Insurance", "Insurance"),
        ("Healthcare", "Healthcare"),
        ("Personal", "Personal"),
        ("Debt", "Debt"),
        ("Retirement", "Retirement"),
        ("Savings", "Savings"),
        ("Education", "Education"),
        ("Entertainment", "Entertainment"),
        ("Savings", "Savings"),
        ("Travel", "Travel"),
        ("Other", "Other"),
    ]

    amount = models.FloatField()
    currency = models.CharField(choices=CURRENCIES)
    category = models.CharField(choices=EXPENSE_CHOICES)
    date = models.DateField()
    details = models.CharField(blank=True, null=True)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        return result

# Todo: Add upcoming expenses model, which will not subtract from the balance until the given date in the future
