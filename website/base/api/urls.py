from django.urls import path, include
from . import views


app_name = "api"

urlpatterns = [
    
    path('cars', views.CarListApiView.as_view(), name='cars'),
    path('car/<int:car_id>', views.CarCRUDView.as_view()),
    path('users', views.UsersListApiView.as_view(), name='users'),
    path('managers', views.ManagerListApiView.as_view(), name='managers'),
    path('user/<int:user_id>', views.UserCRUDView.as_view()),
    path('cities', views.CityListApiView.as_view(), name='cities'),
    path('city/<int:city_id>', views.CityCRUDView.as_view()),
    path('assignment', views.AssignmentView.as_view()),
    path('reports', views.ReportsApiView.as_view()),
    path('tracking', views.TrackingApiView.as_view()),

]