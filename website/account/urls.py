from django.urls import path, include
from . import views


app_name = "account"

urlpatterns = [
    
    path('login', views.login_view, name='login'),
    path('user-login', views.login_view, name='user-login'),
    path('logout', views.logout_view, name='logout'),
]