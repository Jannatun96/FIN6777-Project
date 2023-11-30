from django.urls import path
import wealthwiseapp.views
from wealthwiseapp.views import welcome, user_login, user_logout, user_signup
from .views import financial_goals
urlpatterns = [
    #path('', wealthwiseapp.views.base, name='base'),
    path('', user_login, name='login_redirect'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', user_logout, name='logout'),
    path('financial_goals/', financial_goals, name='financial_goals'),
]
