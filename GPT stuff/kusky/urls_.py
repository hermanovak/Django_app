# #urls.py accounts login logout functionality part

# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView

# app_name = 'accounts'

# urlpatterns = [
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     # add other URL patterns for registration, password reset, etc.
# ]

# #--------------------------------------------------------------------------------------------------------------------------

# #You would then create a template for the QA test form, and a URL pattern to access the form:

# #from django.urls import path
# from django.urls import path
# from .views import qa_test

# app_name = 'medical_physics'

# urlpatterns = [
#     path('qa_test/', qa_test, name='qa_test'),
#     # other URL patterns for Plan prediction and Statistics
# ]

# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('qa_tests/', views.qa_tests, name='qa_tests'),
#     path('plan_prediction/', views.plan_prediction, name='plan_prediction'),
#     path('statistics/', views.statistics, name='statistics'),
# ]


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.login_view, name='login'),
#     path('qa/', views.qa_tests_view, name='qa_tests'),
#     path('qa/daily/<str:date>/', views.daily_qa_view, name='daily_qa'),
#     path('plan/', views.plan_prediction_view, name='plan_prediction'),
#     path('stats/', views.statistics_view, name='statistics'),
# ]


#============================================================================================================================

from django.urls import path
from .views import qa_tests, daily_qa_tests, plan_prediction, statistics


urlpatterns = [
    path('', qa_tests, name='qa