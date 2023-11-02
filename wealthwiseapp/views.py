
from django.shortcuts import render
from .models import FinancialAccount, Expense, Debt

def home(request):
    # Retrieve financial account data from the database
    accounts = FinancialAccount.objects.all()

    # Retrieve expense data from the database
    expenses = Expense.objects.all()

    # Retrieve debt data from the database
    debts = Debt.objects.all()

    context = {
        'accounts': accounts,
        'expenses': expenses,
        'debts': debts,
    }

    return render(request, 'wealthwiseapp/home.html', context)
