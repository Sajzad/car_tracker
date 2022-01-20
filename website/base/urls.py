from django.urls import path, include
from . import views


app_name = "base"

urlpatterns = [
    
    path('', views.home_view, name='home'),
    path('cars', views.cars_view, name='cars'),
    path('users', views.user_view, name='users'),
    path('city', views.city_view, name='city'),
    path('reports', views.reports_view, name='reports'),
    path('tracking', views.tracking_view, name='tracking'),
    path('api/', include('base.api.urls'))
]