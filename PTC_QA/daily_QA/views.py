from django.shortcuts import render, redirect
from .models import DailyTest, DailyTestInput, DLynxMeasurement #must import all needed tables
#from .forms import DailyTestForm, DailyTestInputForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
#import calendar
#from calendar import HTMLCalendar
#from datetime import datetime
from django.utils import timezone
#from django.core.exceptions import ValidationError
#from django.forms import formset_factory #multiple forms in one?
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

#Global variables


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
    datacheck = DailyTest.objects.filter(gantry=1,date_added__contains=timezone.now().date())
    if datacheck.count()==0:
        print("Create new input")
        form = DailyTest()
        form.gantry = 1 
        form.date_added = timezone.now()
        form.save()
    
    last = DailyTest.objects.values().order_by("-index",)[0]
    index = (last['index'])

    if request.method == "POST":

        form = DailyTest.objects.get(pk=index)    
        if request.POST.get('Temp')!=None: 
            form.temperature = request.POST.get('Temp')
        
        if request.POST.get('Pres')!=None: 
            form.pressure = request.POST.get('Pres')

        if request.POST.get('kfactor')!=None: 
            form.kfactor = request.POST.get('kfactor')

        #print(bool(request.POST.getlist('X')))
        if (request.POST.get('X')=='true'): form.laserx = 1
        elif (request.POST.get('X')=='false'): form.laserx = 0

        if request.POST.get('Y')=='true': form.lasery = 1
        elif request.POST.get('Y')=='false': form.lasery=0

        if request.POST.get('Z')=='true': form.laserz = 1
        elif request.POST.get('Z')=='false': form.laserz=0

        if request.POST.get('FlatPanels')=='true': form.flatpanels_check = 1
        elif request.POST.get('FlatPanels')=='false': form.flatpanels_check=0

        if request.POST.get('VisionRT')=='true': form.visionrt_check = 1
        elif request.POST.get('VisionRT')=='false': form.visionrt_check=0

        if request.POST.get('DynR')=='true': form.dynr = 1
        elif request.POST.get('DynR')=='false': form.dynr=0  #pokud jsou disabled, nic se tam nezapisuje   
        form.save()

        #other form - foreign key
        #form2 = DailyTestInput()
        #if request.POST.get('L11595')!='None': form2.input1 = request.POST.get('L11595')
        #form2 = DLynxMeasurement(measurement_id=form.pk)

        #form2 = DLynxMeasurement.objects.create(
        #    measurementid=DailyTest.objects.get(pk=index))
        #form2.save()

        return HttpResponseRedirect('/daily') #?submitted=True') #pass the submitted along
    else:
        
        #form = DailyTestForm(request.POST)
        #form2 = DailyTestInputForm(request.POST)
        print("Not POST")
        
        #if 'submitted' in request.GET: #check whether form was submitted
        #    submitted = True

    return render(request, 'daily_QA/1.html', {
        #context dictionary
        #'dailytestform':form, 
        #'inputform': form2,
        #'submitted':submitted
    })

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})