from django.shortcuts import render
from .models import DailyTest, DLynxReference #must import all needed tables
from .forms import DailyTestForm, DLynxReferenceForm
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime



def home(request):
    data = DailyTest.objects.all()
    context={
        'data': data
    }
    return render(request, 'daily_QA/home.html', context)


def daily(request):
    submitted = False
    if request.method == "POST":
        form = DailyTestForm(request.POST)
        form2 = DLynxReferenceForm(request.POST)
        #lynx = DLynxReference.objects.get(lynx=request.index)
        if form.is_valid():
            #print(form)
            print (form.data['gantry'])
            #lynx = 
            form.save()

            return HttpResponseRedirect('/daily?submitted=True') #pass the submitted along
    else:
        form = DailyTestForm()
        form2 = DLynxReferenceForm(request.POST)
        if 'submitted' in request.GET: #check whether form was submitted
            submitted = True

    return render(request, 'daily_QA/daily copy.html', {
        #context dictionary
        'dailytestform':form, 
        'lynxform': form2,
        'submitted':submitted, 
    })

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})