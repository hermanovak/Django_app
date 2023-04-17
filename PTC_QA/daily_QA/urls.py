from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('/dailyQA', views.daily, name="daily"),
    path('/weeklyQA', views.weekly, name="weekly"),
    path('/monthlyQA', views.monthly, name="monthly"),
]