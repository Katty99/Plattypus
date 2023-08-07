from django.contrib import admin

from Plattypus.finances.models import Income, Expense, Savings

# Register your models here.
to_register = [Income, Expense, Savings]
admin.site.register(to_register)