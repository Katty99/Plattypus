from django.shortcuts import render
from django.views import View

from Plattypus.finances.models import Expense


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
