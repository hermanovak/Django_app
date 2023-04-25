# #views.py loginview part

# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy

# class CustomLoginView(LoginView):
#     template_name = 'accounts/login.html'
#     success_url = reverse_lazy('home')

# # views.py toto asi pracuje viac s databazou!!!
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate, logout
# from django.shortcuts import render, redirect

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

#Next, we'll need to modify the existing views to associate all actions and values 
#with the logged-in user. We can do this by adding a decorator to each view that requires the user to be logged in. 

#This view requires the user to be logged in (@login_required) and 
#associates the new event with the logged-in user (event.user = request.user).

# # views.py
# @login_required
# def create_event(request):
#     if request.method == 'POST':
#         # ...
#         event.user = request.user
#         event.save()
#         return redirect('home')
#     else:
#         # ...

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.forms import Form
# from .models import QAData
# from .forms import TreatmentRoomForm, DailyQAForm

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('qa_tests')
#         else:
#             # Return an error message
#             pass
#     return render(request, 'login.html')

# def qa_tests_view(request):
#     return render(request, 'qa_tests.html')

# def daily_qa_view(request, date):
#     if request.method == 'POST':
#         form = DailyQAForm(request.POST)
#         if form.is_valid():
#             treatment_room = form.cleaned_data['treatment_room']
#             # Save the form data to the database
#             for i in range(1, 11):
#                 description = form.cleaned_data[f'description_{i}']
#                 value_1 = form.cleaned_data[f'value_1_{i}']
#                 value_2 = form.cleaned_data[f'value_2_{i}']
#                 qa_data = QAData(date=date, treatment_room=treatment_room, description=description, value_1=value_1, value_2=value_2, user=request.user)
#                 qa_data.save()
#             return redirect('qa_tests')
#     else:
#         form = DailyQAForm()
#     return render(request, 'daily_qa.html', {'form': form})

# def plan_prediction_view(request):
#     return render(request, 'plan_prediction.html')

# def statistics_view(request):
#     return render(request, 'statistics.html')




# #--------------------------------------------------------------------------------------------------------------------------

# #views.py test form

# #In this example, we have a `qa_test` view that handles the form submission for adding new QA tests. 
# #The view first checks if the request method is POST, and if so, validates the form and saves the QA test to the database. 
# #If the request method is not POST, the view returns a blank form.

# from django.shortcuts import render, redirect
# from .forms import QATestForm

# def qa_test(request):
#     if request.method == 'POST':
#         form = QATestForm(request.POST)
#         if form.is_valid():
#             qa_test = form.save(commit=False)
#             qa_test.user = request.user
#             qa_test.save()
#             return redirect('qa_test')
#     else:
#         form = QATestForm()
#     return render(request, 'qa_test.html', {'form': form})

# #--------------------------------------------------------------------------------------------------------------------------

# #Plan prediction: You can create a form to allow the user to input patient data,and use this data to make plan predictions. 
# #You can create a URL pattern and a view to handle the form submission, and return the plan predictions to the user. 
# #Here's an example:

# from django.shortcuts import render
# from .forms import PlanPredictionForm

# def plan_prediction(request):
#     if request.method == 'POST'

#============================================================================================================================

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import QAForm, PlanForm
from .models import QA, Plan


@login_required(login_url=reverse_lazy('login'))
def qa_tests(request):
    return render(request, 'qa_tests.html')


@login_required(login_url=reverse_lazy('login'))
def daily_qa_tests(request):
    if request.method == 'POST':
        form = QAForm(request.POST)
        if form.is_valid():
            qa = form.save(commit=False)
            qa.user = request.user
            qa.save()
            return redirect('qa_tests')
    else:
        form = QAForm()
    return render(request, 'daily_qa_tests.html', {'form': form})


@login_required(login_url=reverse_lazy('login'))
def plan_prediction(request):
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect('plan_prediction')
    else:
        form = PlanForm()
    return render(request, 'plan_prediction.html', {'form': form})


@login_required(login_url=reverse_lazy('login'))
def statistics(request):
    return render(request, 'statistics.html')

