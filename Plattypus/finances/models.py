from django.db import models

from Plattypus.account.models import Account
from Plattypus.finances.validators import minimum_income

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


# Create your models here.
class Income(models.Model):
    INCOME_SOURCES = [
        ("Work", "Work"),
        ("Gift", "Gift"),
        ("Loan", "Loan"),
        ("Savings", "Savings"),
        ("Donation", "Donation"),
    ]
    amount = models.FloatField(validators=[minimum_income])
    currency = models.CharField(choices=CURRENCIES)
    date = models.DateField()
    details = models.CharField(blank=True, null=True)
    to_profile = models.ForeignKey(Account, on_delete=models.CASCADE)


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
    to_profile = models.ForeignKey(Account, on_delete=models.CASCADE)
