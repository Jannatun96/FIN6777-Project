from django.urls import path
import wealthwiseapp.views
from wealthwiseapp.views import welcome, user_login, user_logout, user_signup

urlpatterns = [
    path('', wealthwiseapp.views.base, name='base'),
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', user_logout, name='logout'),
]
