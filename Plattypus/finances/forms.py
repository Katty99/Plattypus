from django import forms

from Plattypus.finances.models import Income, Expense


class BudgetIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = '__all__'
        exclude = ['user']


class BudgetExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['user']
