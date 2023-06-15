from django.shortcuts import render, redirect
from .models import DailyTest, DailyTestInput, DLynxMeasurement, DailyTestDraft #must import all needed tables
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
from django.contrib.sessions.models import Session


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


def daily(request,gtr):
    print(gtr)
    datacheck = DailyTestDraft.objects.filter(gantry=gtr,date_added__contains=timezone.now().date())
    if datacheck.count()==0:
        print("Create new input")
        form = DailyTestDraft()
        form.gantry = gtr
        form.date_added = timezone.now()
        form.save()
    
    #identify record's index
    listbygantry = DailyTestDraft.objects.values().filter(gantry=gtr)#.order_by("-index",)[0]
    last=listbygantry.order_by('-index')[0]
    index = (last['index'])
    if request.method == "POST":    
        form = DailyTestDraft.objects.get(pk=index)    
        if request.POST.get('Temp')!=None: 
            form.temperature = request.POST.get('Temp')
        
        if request.POST.get('Pres')!=None: 
            form.pressure = request.POST.get('Pres')

        if request.POST.get('kfactor')!=None: 
            form.kfactor = request.POST.get('kfactor')

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
            
        if request.POST.get('LynxID')!=None: 
            form.lynxid = request.POST.get('LynxID')
            
        if request.POST.get('L11595')!=None: 
            form.lynx115_95 = request.POST.get('L11595')

        if request.POST.get('L11599')!=None:
            form.lynx115_99 = request.POST.get('L11599')

        if request.POST.get('L115max')!=None:
            form.lynx115_max = request.POST.get('L115max')

        if request.POST.get('L115avg')!=None:
            form.lynx115_avg = request.POST.get('L115avg')

        if request.POST.get('L14595')!=None: 
            form.lynx145_95 = request.POST.get('L14595')

        if request.POST.get('L14599')!=None:
            form.lynx145_99 = request.POST.get('L14599')

        if request.POST.get('L145max')!=None:
            form.lynx145_max = request.POST.get('L145max')

        if request.POST.get('L145avg')!=None:
            form.lynx145_avg = request.POST.get('L145avg')

        if request.POST.get('L22695')!=None: 
            form.lynx226_95 = request.POST.get('L22695')

        if request.POST.get('L22699')!=None:
            form.lynx226_99 = request.POST.get('L22699')

        if request.POST.get('L226max')!=None:
            form.lynx226_max = request.POST.get('L226max')

        if request.POST.get('L226avg')!=None:
            form.lynx226_avg = request.POST.get('L226avg')

        if request.POST.get('IcID')!=None: 
            form.icid = request.POST.get('IcID')

        if request.POST.get('K100mu')!=None:
            form.ic100_mu = request.POST.get('K100mu')

        if request.POST.get('K100nc')!=None:
            form.ic100_nc = request.POST.get('K100nc')

        if request.POST.get('K170mu')!=None:
            form.ic170_mu = request.POST.get('K170mu')

        if request.POST.get('K170nc')!=None:
            form.ic170_nc = request.POST.get('K170nc')

        if request.POST.get('K226mu')!=None:
            form.ic226_mu = request.POST.get('K226mu')

        if request.POST.get('K226nc')!=None:
            form.ic226_nc = request.POST.get('K226nc')

        if request.POST.get('MlicID')!=None:
            form.mlicid = request.POST.get('MlicID')

        if request.POST.get('MLIC100')!=None:
            form.mlic100_range = request.POST.get('MLIC100')

        if request.POST.get('MLIC170')!=None:
            form.mlic170_range = request.POST.get('MLIC170')

        if request.POST.get('MLIC226')!=None:
            form.mlic226_range = request.POST.get('MLIC226')

        form.save()
        
        return HttpResponseRedirect('/daily'+str(gtr))
    return render(request, 'daily_QA/'+str(gtr)+'.html', {'gtr':gtr})



# def daily1(request):
#     #check if there is already a record for today
#     #gtr = 1
#     if request.method == "POST":
#         form2db(request)
#         #other form - foreign key
#         #form2 = DailyTestInput()
#         #if request.POST.get('L11595')!='None': form2.input1 = request.POST.get('L11595')
#         #form2 = DLynxMeasurement(measurement_id=form.pk)

#         #form2 = DLynxMeasurement.objects.create(
#         #    measurementid=DailyTest.objects.get(pk=index))
#         #form2.save()
#         return HttpResponseRedirect('/daily1') #?submitted=True') #pass the submitted along
#     return render(request, 'daily_QA/1.html', {})

# def daily2(request):
#     #gtr = 2
#     if request.method == "POST":
#         form2db(request)
#         #other form - foreign key
#         #form2 = DailyTestInput()
#         #if request.POST.get('L11595')!='None': form2.input1 = request.POST.get('L11595')
#         #form2 = DLynxMeasurement(measurement_id=form.pk)

#         #form2 = DLynxMeasurement.objects.create(
#         #    measurementid=DailyTest.objects.get(pk=index))
#         #form2.save()
#         return HttpResponseRedirect('/daily2') #?submitted=True') #pass the submitted along
#     return render(request, 'daily_QA/2.html', {})

# def daily3(request):
#     gtr = 3
#     return render(request, 'daily_QA/3.html', {})

# def daily4(request):
#     gtr = 4
#     return render(request, 'daily_QA/4.html', {})

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})