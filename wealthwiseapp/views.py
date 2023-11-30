from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import UserProfile, Expense, OtherBankAccount
from .models import FinancialGoal
from .forms import FinancialGoalForm


def base(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def welcome(request):
    user_profile = UserProfile.objects.get(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    other_bank_accounts = OtherBankAccount.objects.filter(user_profile=user_profile)
    grouped_accounts = {}
    for account in other_bank_accounts:
        if account.bank_name not in grouped_accounts:
            grouped_accounts[account.bank_name] = []
        grouped_accounts[account.bank_name].append(account)

    return render(request, 'welcome.html', {'user_profile': user_profile, 'expenses': expenses,'grouped_accounts': grouped_accounts})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            next_url = request.GET.get('next')
            print(f'Username: {username}, Password: {password}, Next: {next_url}')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                next_url = request.GET.get('next', '')
                if next_url(next_url, allowed_hosts=request.get_host()):
                    return redirect(next_url)
                else:
                    return redirect('welcome')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
        else:
            messages.error(request, 'Error creating the account. Please check the form data.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def financial_goals(request):
    user = request.user
    goals = FinancialGoal.objects.filter(user=user)

    if request.method == 'POST':
        form = FinancialGoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = user
            goal.save()
    else:
        form = FinancialGoalForm()

    return render(request, 'financial_goals.html', {'goals': goals, 'form': form})
