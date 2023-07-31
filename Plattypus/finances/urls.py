from django.urls import path, include

from Plattypus.finances.views import TransactionsView, TransactionDetailsView, TransactionEditView, \
    TransactionDeleteView, AddIncomeView, AddExpenseView

urlpatterns = [
    path('transactions/', TransactionsView.as_view(), name='all_transactions'),
    path('add-income/', AddIncomeView.as_view(), name='add_income'),
    path('add-expense/', AddExpenseView.as_view(), name='add_expense'),
    path('<int:pk>/', include([
        path('details/', TransactionDetailsView.as_view(), name='transaction_details'),
        path('edit/', TransactionEditView.as_view(), name='transaction_edit'),
        path('delete/', TransactionDeleteView.as_view(), name='transaction_delete')
    ])),
]