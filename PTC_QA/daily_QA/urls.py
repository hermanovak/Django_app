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
    path('', views.inlog, name="inlog"), 
    #path('daily_reload/<int:pk>', views.daily_reload, name='daily_reload')
    #path('validate', views.validovat, name='validovat'),
    path('success2/<str:gtr>/', views.success2, name="success2"),
    path('submitted/<int:gtr>/', views.submitted, name="submitted")
]