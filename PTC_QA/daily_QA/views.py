from django.shortcuts import render
from .models import DailyTest, DailyTestInput #must import all needed tables
from .forms import DailyTestForm, DailyTestInputForm
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.core.exceptions import ValidationError
from django.forms import formset_factory #multiple forms in one?


def home(request):
    data = DailyTest.objects.all()
    context={
        'data': data
    }
    return render(request, 'daily_QA/home.html', context)


def daily(request):
    submitted = False
    form = DailyTestForm(request.POST)
    form2 = DailyTestInputForm(request.POST)

    #print (form.data['gantry'])
    if request.method == "POST":
        gantry_val = request.POST.get('treatment-room')
        temperature_val = request.POST.get('temperaturex')
        pressure_val = request.POST.get('pressurex')
        k_val = request.POST.get('k')
        form = Form(DailyTestForm(request.POST,prefix="form"))
        form2 = Form2(DailyTestInputForm(request.POST,prefix="form2"))
        print(form2.data)
        print(form2.fields)

        if form.is_valid() or form2.is_valid():
            f = form.save(commit=False)
            f.gantry = gantry_val
            f.temperature = temperature_val
            f.pressure = pressure_val
            f.kfactor = k_val
            f.save()
            form.save_m2m()
          
            #print(f.cleaned_data)
            print("Validated")

            print(form2.data)
            print(form2.fields)
            form2.save()
            #print("Validated2")
            #print(f2.cleaned_data)
        #     #print(f)
        #     #print(form)
        else:
            #raise ValidationError("Not validating")
            print("Not validating")


        #     #return HttpResponseRedirect('/daily?submitted=True') #pass the submitted along
    else:
        
        form = DailyTestForm(request.POST)
        form2 = DailyTestInputForm(request.POST)
        print("You are here")
        
        if 'submitted' in request.GET: #check whether form was submitted
            submitted = True

    return render(request, 'daily_QA/daily copy 2.html', {
        #context dictionary
        'dailytestform':form, 
        'inputform': form2,
        'submitted':submitted
    })

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})