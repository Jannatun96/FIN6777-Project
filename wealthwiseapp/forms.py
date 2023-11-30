from django import forms
from .models import FinancialGoal

class FinancialGoalForm(forms.ModelForm):
    class Meta:
        model = FinancialGoal
        fields = ['title', 'target_amount', 'is_achieved']
