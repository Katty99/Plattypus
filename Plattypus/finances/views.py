from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from Plattypus.finances.forms import BudgetIncomeForm, BudgetExpenseForm
from Plattypus.finances.models import Expense, Income


def get_transaction(pk):
    transaction = Expense.objects.get(pk=pk)
    return transaction


# Create your views here.
class TransactionsView(View):
    def get(self, request):
        user_transactions = Expense.objects.all()
        context = {'user_transactions': user_transactions}
        return render(request, template_name='finances/history-page.html', context=context)


class TransactionDetailsView(View):
    def get(self, request, pk):
        transaction = get_transaction(pk)
        context = {'transaction': transaction}
        return render(request, template_name='finances/transaction-detail.html', context=context)


class TransactionEditView(View):
    def get(self, request, pk):
        transaction = get_transaction(pk)
        context = {'transaction': transaction}
        return render(request, template_name='finances/transaction-edit.html', context=context)


class TransactionDeleteView(View):
    def get(self, request, pk):
        transaction = get_transaction(pk)
        context = {'transaction': transaction}
        return render(request, template_name='finances/transaction-delete.html', context=context)


class AddExpenseView(LoginRequiredMixin, CreateView):
    template_name = 'finances/add_expense.html'
    form_class = BudgetExpenseForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Expense(user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user for the expense
        return super().form_valid(form)


class AddIncomeView(LoginRequiredMixin, CreateView):
    template_name = 'finances/add_income.html'
    form_class = BudgetIncomeForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Income(user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user for the income
        return super().form_valid(form)
