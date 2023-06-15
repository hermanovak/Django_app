from django.urls import path
from . import views

app_name='daily_QA'

urlpatterns = [
    path('home', views.home, name="home"),
    path('gtrselect', views.gtrselect, name="gtrselect"),
    path('daily<int:gtr>', views.daily, name="daily"), #path converter
    path('weekly', views.weekly, name="weekly"),
    path('monthly', views.monthly, name="monthly"),
    path('', views.inlog, name="inlog")
]