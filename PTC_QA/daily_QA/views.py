from django.shortcuts import render, redirect
from .models import DailyTest, DailyTestInput #must import all needed tables
from .forms import DailyTestForm, DailyTestInputForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.forms import formset_factory #multiple forms in one?
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

#@login_required   
def inlog(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request, data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            print(user)
            login(request, user)
            return redirect('daily_QA:home')
    else:
        loginform = AuthenticationForm(request)

    return render(request,'daily_QA/inlog.html',{
    'loginform':loginform})

def home(request):
    return render(request, 'daily_QA/home.html')


def gtrselect(request):

    return render(request, 'daily_QA/gtrselect.html')


def daily(request):
    submitted = False
   
    #form = DailyTestForm(request.POST)
    #form2 = DailyTestInputForm(request.POST)
    #print(request.user.id)

    #print (form.data['gantry']) 
    if request.method == "POST":

        temperature_val = request.POST.get('Temp')
        pressure_val = request.POST.get('Pres')
        print(temperature_val)
        print(pressure_val)

        form = DailyTestForm(request.POST)
        form2 = DailyTestInputForm(request.POST)


        if form.is_valid() or form2.is_valid():
            f = form.save(commit=False)
            #f.gantry = gantry_val
            f.temperature = temperature_val
            f.pressure = pressure_val
            #f.kfactor = k_val
            f.date_added = timezone.now()
            f.save()
            form.save_m2m()

            #f2 = form2.save(commit=False)
            idx = DailyTest.objects.all().order_by("-index",)[0]
            #idx_int = Convert.ToInt32(idx.ExecuteScalar());
            #idx_int=int(idx)
            #print(type(idx_int))
            #f2.indexid = idx+1
            #f2.save()
            #print(request.user)
            #form2.save(commit=False)
            #form2.indexid=gantry_val
            #form2.save_m2m()
          
            #print(f.cleaned_data)
            print("Validated")
        else:
            #raise ValidationError("Not validating")
            print("Not validating")


            return HttpResponseRedirect('/daily?submitted=True') #pass the submitted along
    else:
        
        #form = DailyTestForm(request.POST)
        #form2 = DailyTestInputForm(request.POST)
        print("You are here")
        form = DailyTestForm()
        form2 = DailyTestInputForm()
        
        if 'submitted' in request.GET: #check whether form was submitted
            submitted = True

    return render(request, 'daily_QA/1.html', {
        #context dictionary
        'dailytestform':form, 
        'inputform': form2,
        'submitted':submitted
    })

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})