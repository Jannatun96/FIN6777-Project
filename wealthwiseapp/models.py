from django.db import models
from django.contrib.auth.models import User



class FinancialAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    institution = models.CharField(max_length=100)

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return f"{self.amount} - {self.category.name} - {self.description} - {self.date}"

class Debt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    remaining_payments = models.IntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    routing_number = models.CharField(max_length=9)
    bank_account_number = models.CharField(max_length=12)
    credit_card_debt = models.DecimalField(max_digits=10, decimal_places=2)
    mortgage_value = models.DecimalField(max_digits=8, decimal_places=2)
    car_loan = models.DecimalField(max_digits=8, decimal_places=2)
    student_loan = models.DecimalField(max_digits=8, decimal_places=2)
    investment_portfolio_value = models.DecimalField(max_digits=7, decimal_places=2)
    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['email', 'routing_number', 'bank_account_number']
    def __str__(self):
        return self.user
