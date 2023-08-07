from django.urls import path, include

from Plattypus.finances.views import TransactionsView, TransactionDetailsView, TransactionEditView, \
    TransactionDeleteView, AddIncomeView, AddExpenseView, AddSavingsView, SavingsView, EditSavingsView, \
    DeleteSavingsView

urlpatterns = [
    path('transactions/', TransactionsView.as_view(), name='all_transactions'),
    path('add-income/', AddIncomeView.as_view(), name='add_income'),
    path('add-expense/', AddExpenseView.as_view(), name='add_expense'),
    path('add-savings/', AddSavingsView.as_view(), name='add_savings'),
    path('<int:pk>/', include([
        path('details/', TransactionDetailsView.as_view(), name='transaction_details'),
        path('edit/', TransactionEditView.as_view(), name='transaction_edit'),
        path('delete/', TransactionDeleteView.as_view(), name='transaction_delete')
    ])),
    path('savings/<int:pk>/', include([
            path('edit/', EditSavingsView.as_view(), name='savings_edit'),
            path('delete/', DeleteSavingsView.as_view(), name='savings_delete')
        ])),
]