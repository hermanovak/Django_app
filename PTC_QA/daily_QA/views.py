from django.shortcuts import render
from .models import DailyTest #must import all needed tables
from .forms import DailyTestForm
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
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/daily?submitted=True') #pass the submitted along
    else:
        form = DailyTestForm
        if 'submitted' in request.GET: #check whether form was submitted
            submitted = True

    return render(request, 'daily_QA/daily.html', {
        #context dictionary
        'form':form, 
        'submitted':submitted
    })

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})