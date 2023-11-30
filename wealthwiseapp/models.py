from django.db import models
from django.contrib.auth.models import User



class FinancialAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
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
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    credit_card_debt = models.DecimalField(max_digits=10, decimal_places=2)
    mortgage_value = models.DecimalField(max_digits=8, decimal_places=2)
    car_loan = models.DecimalField(max_digits=8, decimal_places=2)
    student_loan = models.DecimalField(max_digits=8, decimal_places=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cryptocurrency_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stocks_value = models.DecimalField(max_digits=8, decimal_places=2, default =0.0)
    bonds_value = models.DecimalField(max_digits=8, decimal_places=2, default = 0.0)
    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['email', 'routing_number', 'bank_account_number']
    def __str__(self):
        return self.user

class OtherBankAccount(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user_profile.user.username}'s {self.account_type} Account at {self.bank_name}"

class FinancialGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s {self.title} Goal"
