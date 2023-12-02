from django.urls import path # import path function
from . import views # import our views

urlpatterns = [
    path('accounts/<int:first_account_number>/<slug:second_account_number>/', views.getData), # GET accounts URL
    path('add/<int:first_account_number>/<slug:second_account_number>/', views.addItem) # POST URL
]

# Test Accounts
# 88661198/GB27OKKM74860470093867