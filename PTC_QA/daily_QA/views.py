from django.shortcuts import render, redirect
from .models import DailyTest, DailyTestInput, DLynxMeasurement, DailyTestDraft #must import all needed tables
#from .forms import DailyTestForm, DailyTestInputForm
from django.http import HttpResponseRedirect
#from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
#import calendar
#from calendar import HTMLCalendar
#from datetime import datetime
from django.utils import timezone
#from django.core.exceptions import ValidationError
#from django.forms import formset_factory #multiple forms in one?
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
    datacheck = DailyTestDraft.objects.filter(gantry=gtr,date_added__contains=timezone.now().date())
    if datacheck.count()==0:
        print("Create new input")
        form = DailyTestDraft.objects.create(gantry=gtr, date_added = timezone.now())
    
    #identify record's index
    listbygantry = DailyTestDraft.objects.values().filter(gantry=gtr)#.order_by("-index",)[0]
    last=listbygantry.order_by('-index')[0]
    index = (last['index'])
    if request.method == "POST":    
        form = DailyTestDraft.objects.get(pk=index)
        form2 = DailyTestInput(indexid=form)
        form2.save()
        #lynxform70 = DLynxMeasurement(energy=70, measurementid=form)
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
            form.lynxid = request.POST.get('LynxID')
            #lynxform70.LynxID = request.POST.get('LynxID')
            
        if request.POST.get('L7095')!=None: 
            form.lynx70_95 = request.POST.get('L7095')
            #lynxform70.val95 = request.POST.get('L7095')

        if request.POST.get('L7099')!=None:
            form.lynx70_99 = request.POST.get('L7099')
            #lynxform70.val99 = request.POST.get('L7099')

        if request.POST.get('L70max')!=None:
            form.lynx70_max = request.POST.get('L70max')
            #lynxform70.max = request.POST.get('L70max')

        if request.POST.get('L70avg')!=None:
            form.lynx70_avg = request.POST.get('L70avg')
            #lynxform70.avg = request.POST.get('L70avg')
            
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

        if request.POST.get('K70mu')!=None:
            form.ic70_mu = request.POST.get('K70mu')

        if request.POST.get('K70nc')!=None:
            form.ic100_nc = request.POST.get('K70nc')

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

        if request.POST.get('MLIC70')!=None:
            form.mlic70_range = request.POST.get('MLIC70')

        if request.POST.get('MLIC100')!=None:
            form.mlic100_range = request.POST.get('MLIC100')

        if request.POST.get('MLIC170')!=None:
            form.mlic170_range = request.POST.get('MLIC170')

        if request.POST.get('MLIC226')!=None:
            form.mlic226_range = request.POST.get('MLIC226')

        form.save()
        #lynxform70.save()
        
        # if request.POST.get('LynxID')!=None: 
        #     lynxid = request.POST.get('LynxID')
        #print(type(form.index))


        
        #form2.indexid_id = form
        #form2recordHandle = form2.Objects.Create(indexid=form)
        #print(type(form2.indexid))
        # form2 = DailyTestInput(energyID = 1, input1 = 1, input2 = 1, input3 = 1, input4 = 1 , configID = 1, indexid_id=form)
        # form2.save()
        #form2.configid = lynxid
        #form2.save()  
        #print(form2.index.id)
        
        return HttpResponseRedirect('/daily'+str(gtr))
    return render(request, 'daily_QA/'+str(gtr)+'.html', {'gtr':gtr})


def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})