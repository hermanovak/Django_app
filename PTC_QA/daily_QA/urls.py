from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('daily', views.daily, name="daily"),
    path('weekly', views.weekly, name="weekly"),
    path('monthly', views.monthly, name="monthly"),
]