from django.db import models

class FinancialAccount(models.Model):
    objects = None
    account_name = models.CharField(max_length=255)
    account_balance = models.DecimalField(max_digits=10, decimal_places=2)

class Expense(models.Model):
    objects = None
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class Debt(models.Model):
    objects = None
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

