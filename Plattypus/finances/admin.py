from django.contrib import admin

from Plattypus.finances.models import Income, Expense

# Register your models here.
to_register = [Income, Expense]
admin.site.register(to_register)