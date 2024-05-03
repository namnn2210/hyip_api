from django.urls import path, include
from .views import signup, login, account

urlpatterns = [
    path('signup', signup, name='signup'),
    path('login', login, name='login'),
    path('account', account, name='account'),
]