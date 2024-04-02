from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name='daily_QA'
#from daily_QA.views import daily_reload

urlpatterns = [
    path('home', views.home, name="home"),
    path('gtrselect', views.gtrselect, name="gtrselect"),
    path('daily<int:gtr>', views.daily, name="daily"), #path converter
    path('weekly', views.weekly, name="weekly"),
    path('monthly', views.monthly, name="monthly"),
    path('login', views.inlog, name="inlog"), 
    path('daily_reload', views.daily_reload, name='daily_reload'), #'daily_reload/<int:pk>'
    #path('validate', views.validovat, name='validovat'),
    #path('success2/<str:gtr>/', views.success2, name="success2"),
    path('success2', views.success2, name="success2"),
    path('submitted', views.submitted, name="submitted"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]