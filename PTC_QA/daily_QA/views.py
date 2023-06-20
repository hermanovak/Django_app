from django.shortcuts import render, redirect
from .models import DailyTest, DailyTestInput, DLynxMeasurement, DailyTestDraft, DIcMeasurement, DMlicMeasurement #must import all needed tables
from django.http import HttpResponseRedirect
#from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
#from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib import messages
from django.contrib.sessions.models import Session


#Global variables


#@login_required   
def inlog(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request, data=request.POST)
        if loginform.is_valid():
            user = loginform.get_user()
            #print(user)
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
    datacheck = DailyTest.objects.filter(gantry=gtr,date_added__contains=timezone.now().date())
    if datacheck.count()==0:
        print("Create new input")
        form = DailyTest.objects.create(gantry=gtr, date_added = timezone.now())
        if gtr==3: 
            lynxform70 = DLynxMeasurement.objects.create(energy=70, measurementid=form)
            icform70 = DIcMeasurement.objects.create(energy=70, measurementid=form)
            mlicform70 = DMlicMeasurement.objects.create(energy=70, measurementid=form)
        lynxform115 = DLynxMeasurement.objects.create(energy=115, measurementid=form)
        lynxform145 = DLynxMeasurement.objects.create(energy=145, measurementid=form)
        lynxform226 = DLynxMeasurement.objects.create(energy=226, measurementid=form)
        icform100 = DIcMeasurement.objects.create(energy=100, measurementid=form)
        icform170 = DIcMeasurement.objects.create(energy=170, measurementid=form)
        icform226 = DIcMeasurement.objects.create(energy=226, measurementid=form)
        mlicform100 = DMlicMeasurement.objects.create(energy=100, measurementid=form)
        mlicform170 = DMlicMeasurement.objects.create(energy=170, measurementid=form)
        mlicform226 = DMlicMeasurement.objects.create(energy=226, measurementid=form)
    
    #identify record's index
    listbygantry = DailyTest.objects.values().filter(gantry=gtr)#.order_by("-index",)[0]
    last=listbygantry.order_by('-index')[0]
    index = (last['index'])
    form = DailyTest.objects.get(pk=index)
    if gtr==3:
        lynxform70 = DLynxMeasurement.objects.get(measurementid=index,energy=70)
        icform70 = DIcMeasurement.objects.get(measurementid=index,energy=70)
        mlicform70 = DMlicMeasurement.objects.get(measurementid=index,energy=70)
    lynxform115 = DLynxMeasurement.objects.get(measurementid=index,energy=115)
    lynxform145 = DLynxMeasurement.objects.get(measurementid=index,energy=145)
    lynxform226 = DLynxMeasurement.objects.get(measurementid=index,energy=226)
    icform100 = DIcMeasurement.objects.get(measurementid=index,energy=100)
    icform170 = DIcMeasurement.objects.get(measurementid=index,energy=170)
    icform226 = DIcMeasurement.objects.get(measurementid=index,energy=226)
    mlicform100 = DMlicMeasurement.objects.get(measurementid=index,energy=100)
    mlicform170 = DMlicMeasurement.objects.get(measurementid=index,energy=170)
    mlicform226 = DMlicMeasurement.objects.get(measurementid=index,energy=226)

    if request.method == "POST":    
        
        #form2 = DailyTestInput(indexid=form)
        #form2.save()
        
        #lynxform70.save()
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
            #form.lynxid = request.POST.get('LynxID')
            if gtr==3:
                lynxform70.lynxid = request.POST.get('LynxID')
            lynxform115.lynxid = request.POST.get('LynxID')
            lynxform145.lynxid = request.POST.get('LynxID')
            lynxform226.lynxid = request.POST.get('LynxID')
            
        if request.POST.get('L7095')!=None: 
            #form.lynx70_95 = request.POST.get('L7095')
            lynxform70.val95 = request.POST.get('L7095')

        if request.POST.get('L7099')!=None:
            #form.lynx70_99 = request.POST.get('L7099')
            lynxform70.val99 = request.POST.get('L7099')

        if request.POST.get('L70max')!=None:
            #form.lynx70_max = request.POST.get('L70max')
            lynxform70.max = request.POST.get('L70max')

        if request.POST.get('L70avg')!=None:
            #form.lynx70_avg = request.POST.get('L70avg')
            lynxform70.avg = request.POST.get('L70avg')
            
        if request.POST.get('L11595')!=None: 
            #form.lynx115_95 = request.POST.get('L11595')
            lynxform115.val95 = request.POST.get('L11595')

        if request.POST.get('L11599')!=None:
            #form.lynx115_99 = request.POST.get('L11599')
            lynxform115.val99 = request.POST.get('L11599')

        if request.POST.get('L115max')!=None:
            #form.lynx115_max = request.POST.get('L115max')
            lynxform115.max = request.POST.get('L115max')

        if request.POST.get('L115avg')!=None:
            #form.lynx115_avg = request.POST.get('L115avg')
            lynxform115.avg = request.POST.get('L115avg')

        if request.POST.get('L14595')!=None: 
            #form.lynx145_95 = request.POST.get('L14595')
            lynxform145.val95 = request.POST.get('L14595')

        if request.POST.get('L14599')!=None:
            #form.lynx145_99 = request.POST.get('L14599')
            lynxform145.val99 = request.POST.get('L14599')

        if request.POST.get('L145max')!=None:
            lynxform145.max = request.POST.get('L145max')

        if request.POST.get('L145avg')!=None:
            lynxform145.avg = request.POST.get('L145avg')

        if request.POST.get('L22695')!=None: 
            lynxform226.val95 = request.POST.get('L22695')

        if request.POST.get('L22699')!=None:
            lynxform226.val99 = request.POST.get('L22699')

        if request.POST.get('L226max')!=None:
            lynxform226.max = request.POST.get('L226max')

        if request.POST.get('L226avg')!=None:
            lynxform226.avg = request.POST.get('L226avg')

        if request.POST.get('IcID')!=None: 
            icform70.ic_id = request.POST.get('IcID')

        if request.POST.get('K70mu')!=None:
            icform70.response_mu = request.POST.get('K70mu')

        if request.POST.get('K70nc')!=None:
            icform70.response_nc = request.POST.get('K70nc')

        if request.POST.get('K100mu')!=None:
            icform100.response_mu = request.POST.get('K100mu')

        if request.POST.get('K100nc')!=None:
            icform100.response_nc = request.POST.get('K100nc')

        if request.POST.get('K170mu')!=None:
            icform170.response_mu = request.POST.get('K170mu')

        if request.POST.get('K170nc')!=None:
            icform170.response_nc = request.POST.get('K170nc')

        if request.POST.get('K226mu')!=None:
            icform226.response_mu = request.POST.get('K226mu')

        if request.POST.get('K226nc')!=None:
            icform226.response_nc = request.POST.get('K226nc')

        if request.POST.get('MlicID')!=None:
            #form.mlicid = request.POST.get('MlicID')
            if gtr==3:
                mlicform70.mlicid = request.POST.get('MlicID')
            mlicform100.mlicid = request.POST.get('MlicID')
            mlicform170.mlicid = request.POST.get('MlicID')
            mlicform226.mlicid = request.POST.get('MlicID')

        if request.POST.get('MLIC70')!=None:
            mlicform70.range = request.POST.get('MLIC70')

        if request.POST.get('MLIC100')!=None:
            mlicform100.range = request.POST.get('MLIC100')

        if request.POST.get('MLIC170')!=None:
            mlicform170.range = request.POST.get('MLIC170')

        if request.POST.get('MLIC226')!=None:
            mlicform226.range = request.POST.get('MLIC226')

        form.save()
        if gtr==3:
            lynxform70.save()
            icform70.save()
            mlicform70.save()
        lynxform115.save()
        lynxform145.save()
        lynxform226.save()
        icform100.save()
        icform170.save()
        icform226.save()
        mlicform100.save()
        mlicform170.save()
        mlicform226.save()

                
        return HttpResponseRedirect('/daily'+str(gtr))
    return render(request, 'daily_QA/'+str(gtr)+'.html', {'gtr':gtr})


def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})