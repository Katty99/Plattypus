from itertools import chain

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from Plattypus.finances.forms import BudgetIncomeForm, BudgetExpenseForm, SavingsForm
from Plattypus.finances.models import Expense, Income, Savings


# Create your views here.
class TransactionsView(LoginRequiredMixin, ListView):
    template_name = 'finances/history-page.html'
    context_object_name = 'transactions'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        transactions = list(Income.objects.filter(user=user)) + list(Expense.objects.filter(user=user))
        transactions.sort(key=lambda x: x.date, reverse=True)

        return transactions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context


class TransactionDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'finances/transaction-detail.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        user = self.request.user
        incomes = Income.objects.filter(user=user)
        expenses = Expense.objects.filter(user=user)
        transactions = list(chain(incomes, expenses))
        return transactions

    def get_object(self, queryset=None):
        transaction_pk = self.kwargs.get('pk')

        try:
            transaction = Income.objects.get(pk=transaction_pk, user=self.request.user)
        except Income.DoesNotExist:
            transaction = Expense.objects.get(pk=transaction_pk, user=self.request.user)

        return transaction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context


class TransactionEditView(LoginRequiredMixin, UpdateView):
    template_name = 'finances/transaction-edit.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('all_transactions')

    def get_object(self, queryset=None):
        transaction_pk = self.kwargs.get('pk')
        user = self.request.user

        try:
            transaction = Income.objects.get(pk=transaction_pk, user=user)
        except Income.DoesNotExist:
            transaction = get_object_or_404(Expense, pk=transaction_pk, user=user)

        return transaction

    def get_form(self, form_class=None):
        transaction = self.get_object()

        if isinstance(transaction, Income):
            return BudgetIncomeForm(**self.get_form_kwargs())
        elif isinstance(transaction, Expense):
            return BudgetExpenseForm(**self.get_form_kwargs())

        return super().get_form(form_class)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'finances/transaction-delete.html'
    context_object_name = 'transaction'
    success_url = reverse_lazy('all_transactions')

    def get_object(self, queryset=None):
        transaction_pk = self.kwargs.get('pk')
        user = self.request.user
        transaction = get_object_or_404(Income, pk=transaction_pk, user=user) or \
                      get_object_or_404(Expense, pk=transaction_pk, user=user)
        return transaction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context


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


class AddSavingsView(LoginRequiredMixin, CreateView):
    template_name = 'finances/add_savings.html'
    form_class = SavingsForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Savings(user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SavingsView(LoginRequiredMixin, DetailView):
    template_name = 'account/dashboard.html'
    context_object_name = 'savings'

    def get_queryset(self):
        user = self.request.user
        savings = Savings.objects.filter(user=user)
        return savings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context


class EditSavingsView(LoginRequiredMixin, UpdateView):
    template_name = 'finances/edit_savings.html'
    form_class = SavingsForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Savings(user=self.request.user)
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteSavingsView(LoginRequiredMixin, DeleteView):
    template_name = 'finances/delete_savings.html'
    form_class = SavingsForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = Savings(user=self.request.user)
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        return context
