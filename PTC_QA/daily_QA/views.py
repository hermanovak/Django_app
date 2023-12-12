from django.shortcuts import render, redirect
from .models import DailyTest, DailyTestInput, DLynxMeasurement, DailyTestDraft, DIcMeasurement, DMlicMeasurement #must import all needed tables
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
#from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib import messages
from django.contrib.sessions.models import Session
#from json import dumps as jdumps
from itertools import chain
from django import forms
from django.db.models import Q

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

        #if gtr==3: 
        #    lynxform70 = DLynxMeasurement.objects.create(energy=70, measurementid=form)
        #    icform70 = DIcMeasurement.objects.create(energy=70, measurementid=form)
        #    mlicform70 = DMlicMeasurement.objects.create(energy=70, measurementid=form)

        #lynxform115 = DLynxMeasurement.objects.create(energy=115, measurementid=form)
        #lynxform145 = DLynxMeasurement.objects.create(energy=145, measurementid=form)
        #lynxform226 = DLynxMeasurement.objects.create(energy=226, measurementid=form)
        #icform100 = DIcMeasurement.objects.create(energy=100, measurementid=form)
        #icform170 = DIcMeasurement.objects.create(energy=170, measurementid=form)
        #icform226 = DIcMeasurement.objects.create(energy=226, measurementid=form)
        #mlicform100 = DMlicMeasurement.objects.create(energy=100, measurementid=form)
        #mlicform170 = DMlicMeasurement.objects.create(energy=170, measurementid=form)
        #mlicform226 = DMlicMeasurement.objects.create(energy=226, measurementid=form)
    
    #print(request.POST.get('reload'))
    
        
    
    #identify record's index
    listbygantry = DailyTestDraft.objects.values().filter(gantry=gtr)#.order_by("-index",)[0]
    last=listbygantry.order_by('-index')[0]
    index = (last['index'])
    form = DailyTestDraft.objects.get(pk=index)
    #if gtr==3:
    #    lynxform70 = DLynxMeasurement.objects.get(measurementid=index,energy=70)
    #    icform70 = DIcMeasurement.objects.get(measurementid=index,energy=70)
    #    mlicform70 = DMlicMeasurement.objects.get(measurementid=index,energy=70)
    #lynxform115 = DLynxMeasurement.objects.get(measurementid=index,energy=115)
    #lynxform145 = DLynxMeasurement.objects.get(measurementid=index,energy=145)
    #lynxform226 = DLynxMeasurement.objects.get(measurementid=index,energy=226)
    #icform100 = DIcMeasurement.objects.get(measurementid=index,energy=100)
    #icform170 = DIcMeasurement.objects.get(measurementid=index,energy=170)
    #icform226 = DIcMeasurement.objects.get(measurementid=index,energy=226)
    #mlicform100 = DMlicMeasurement.objects.get(measurementid=index,energy=100)
    #mlicform170 = DMlicMeasurement.objects.get(measurementid=index,energy=170)
    #mlicform226 = DMlicMeasurement.objects.get(measurementid=index,energy=226)

    #print(data)
    #if request.POST.values()!=None:
    #    lst=list(request.POST.values())
    #print(type(lst))
    #print(list.__getitem__[0])
    #print(HttpResponse)
    if request.method == "POST":   

        #if request.POST.get('reload'):
            #listbygantry = DailyTest.objects.values().filter(gantry=gtr)#.order_by("-index",)[0]
            #last=listbygantry.order_by('-index')[0]
            #print(last['temperature'])
            #print(request.POST.get('reload'))
            
            #print(rld)

        #data=request.POST
        #if (data.indexOf('115')>= 0):
        #    print('E is 115')   
        
        #device = ['ic', 'lynx', 'mlic']
        #energy = [70,100,145,170,226]
        #val = ['95', '99', 'avg', 'max', 'nc', 'mu', 'range']

        #for a in device:
        #    for b in energy:
        #        for c in val:
        #            if a=='L':
        #                break
        #            data=a+str(b)+c
        #            form = a+'form'+str(b)
        #            print(form)
        #            value='val'+str(c)
        #            print(value)
        #            form.response_mu = request.POST.get('L'+str(b)+c)
        #            print(form.value)


                    

        if request.POST.get('Temp'): 
            form.temperature = request.POST.get('Temp')
        elif request.POST.get('Temp')=='': #pokud user zapise a na to vymaze, ulozi se prazdna
            form.temperature = None

        if request.POST.get('Pres'): 
            form.pressure = request.POST.get('Pres')

        if request.POST.get('kfactor'): 
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
            #if gtr==3:
            #    lynxform70.lynxid = request.POST.get('LynxID')
            #lynxform115.lynxid = request.POST.get('LynxID')
            #lynxform145.lynxid = request.POST.get('LynxID')
            #lynxform226.lynxid = request.POST.get('LynxID')
            
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
            #lynxform115.val95 = request.POST.get('L11595')

        if request.POST.get('L11599')!=None:
            form.lynx115_99 = request.POST.get('L11599')
            #lynxform115.val99 = request.POST.get('L11599')

        if request.POST.get('L115max')!=None:
            form.lynx115_max = request.POST.get('L115max')
            #lynxform115.max = request.POST.get('L115max')

        if request.POST.get('L115avg')!=None:
            form.lynx115_avg = request.POST.get('L115avg')
            #lynxform115.avg = request.POST.get('L115avg')

        if request.POST.get('L14595')!=None: 
            form.lynx145_95 = request.POST.get('L14595')
            #lynxform145.val95 = request.POST.get('L14595')

        if request.POST.get('L14599')!=None:
            form.lynx145_99 = request.POST.get('L14599')
            #lynxform145.val99 = request.POST.get('L14599')

        if request.POST.get('L145max')!=None:
            #print(request.POST.get('L145max'))
            form.lynx145_max = request.POST.get('L145max')
            #lynxform145.max = request.POST.get('L145max')

        if request.POST.get('L145avg')!=None:
            form.lynx145_avg = request.POST.get('L145avg')
            #lynxform145.avg = request.POST.get('L145avg')

        if request.POST.get('L22695')!=None: 
            form.lynx226_95 = request.POST.get('L22695')
            #lynxform226.val95 = request.POST.get('L22695')

        if request.POST.get('L22699')!=None:
            form.lynx226_99 = request.POST.get('L22699')
            #lynxform226.val99 = request.POST.get('L22699')

        if request.POST.get('L226max')!=None:
            form.lynx226_max = request.POST.get('L226max')
            # lynxform226.max = request.POST.get('L226max')

        if request.POST.get('L226avg')!=None:
            form.lynx226_avg = request.POST.get('L226avg')
            #lynxform226.avg = request.POST.get('L226avg')

        if request.POST.get('IcID')!=None:
            form.icid = request.POST.get('IcID')
            #if gtr==3: 
            #    icform70.ic_id = request.POST.get('IcID')
            #icform100.ic_id = request.POST.get('IcID')
            #icform170.ic_id = request.POST.get('IcID')
            #icform226.ic_id = request.POST.get('IcID')

        if request.POST.get('K70mu')!=None:
            form.ic70_mu = request.POST.get('K70mu')
            #icform70.response_mu = request.POST.get('K70mu')

        if request.POST.get('K70nc')!=None:
            form.ic70_nc = request.POST.get('K70nc')
            #icform70.response_nc = request.POST.get('K70nc')

        if request.POST.get('K100mu')!=None:
            form.ic100_mu = request.POST.get('K100mu')
            #icform100.response_mu = request.POST.get('K100mu')

        if request.POST.get('K100nc')!=None:
            form.ic100_nc = request.POST.get('K100nc')
            #icform100.response_nc = request.POST.get('K100nc')

        if request.POST.get('K170mu')!=None:
            form.ic170_mu = request.POST.get('K170mu')
            #icform170.response_mu = request.POST.get('K170mu')

        if request.POST.get('K170nc')!=None:
            form.ic170_nc = request.POST.get('K170nc')
            #icform170.response_nc = request.POST.get('K170nc')

        if request.POST.get('K226mu')!=None:
            form.ic226_mu = request.POST.get('K226mu')
            #icform226.response_mu = request.POST.get('K226mu')

        if request.POST.get('K226nc')!=None:
            form.ic226_nc = request.POST.get('K226nc')
            #icform226.response_nc = request.POST.get('K226nc')

        if request.POST.get('MlicID')!=None:
            form.mlicid = request.POST.get('MlicID')
            #if gtr==3:
            #    mlicform70.mlicid = request.POST.get('MlicID')
            #mlicform100.mlicid = request.POST.get('MlicID')
            #mlicform170.mlicid = request.POST.get('MlicID')
            #mlicform226.mlicid = request.POST.get('MlicID')

        if request.POST.get('MLIC70')!=None:
            form.mlic70_range = request.POST.get('MLIC70')
            #mlicform70.range = request.POST.get('MLIC70')

        if request.POST.get('MLIC100')!=None:
            form.mlic100_range = request.POST.get('MLIC100')
            #mlicform100.range = request.POST.get('MLIC100')

        if request.POST.get('MLIC170')!=None:
            form.mlic170_range = request.POST.get('MLIC170')
            #mlicform170.range = request.POST.get('MLIC170')

        if request.POST.get('MLIC226')!=None:
            form.mlic226_range = request.POST.get('MLIC226')
            #mlicform226.range = request.POST.get('MLIC226')

        form.save()
        #if gtr==3:
        #    lynxform70.save()
        #    icform70.save()
        #    mlicform70.save()
        #lynxform115.save()
        #lynxform145.save()
        #lynxform226.save()
        #icform100.save()
        #icform170.save()
        #icform226.save()
        #mlicform100.save()
        #mlicform170.save()
        #mlicform226.save()

        #Joining querysets:
        #hlavicka = DailyTest.objects.values().filter(pk=index)
        #lynx115 = DLynxMeasurement.objects.values().filter(measurementid=index,energy=115)
        #print(list(chain(hlavicka, lynx115)))

        if request.POST.get('tlacitko')=='Submit':
            #if request.POST.get('checksAllChecks')=='1':
                #form.validate = 1
            #submit code here
            #print("Jdeme validovat") #check

            # Check if the DailyTest instance already exists
            existing_hlavicka_instance = DailyTest.objects.filter(
                date_added=form.date_added,
                gantry=form.gantry,
                visionrt_check=form.visionrt_check,
                flatpanels_check=form.flatpanels_check,
                dynr=form.dynr,
                temperature=form.temperature,
                pressure=form.pressure,
                kfactor=form.kfactor,
                laserx=form.laserx,
                lasery=form.lasery,
                laserz=form.laserz
            ).first()

            # Create hlavicka_instance if it doesn't already exist
            if existing_hlavicka_instance is None:
                hlavicka_instance = DailyTest.objects.create(
                    date_added=form.date_added,
                    gantry=form.gantry,
                    visionrt_check=form.visionrt_check,
                    flatpanels_check=form.flatpanels_check,
                    dynr=form.dynr,
                    temperature=form.temperature,
                    pressure=form.pressure,
                    kfactor=form.kfactor,
                    laserx=form.laserx,
                    lasery=form.lasery,
                    laserz=form.laserz
                )
                
            else:
                # Use the existing instance
                hlavicka_instance = existing_hlavicka_instance
            hlavicka_instance.save()

            for energy_var in [70,115,145,226]:
                    
                existing_lynx_instance = DLynxMeasurement.objects.filter(
                    Q(energy=energy_var) &
                    Q(measurementid=hlavicka_instance) &
                    Q(lynxid=form.lynxid)
                ).first()
                
                if existing_lynx_instance is None:

                    lynx_instance = DLynxMeasurement(
                    energy = energy_var,
                    measurementid=hlavicka_instance,
                    lynxid = form.lynxid,
                    val99 = getattr(form,'lynx'+str(energy_var)+'_99'),
                    val95 = getattr(form,'lynx'+str(energy_var)+'_95'),
                    avg = getattr(form,'lynx'+str(energy_var)+'_avg'),
                    max = getattr(form,'lynx'+str(energy_var)+'_max')
                    )
                else:
                # Use the existing instance
                    lynx_instance = existing_lynx_instance
                lynx_instance.save()

            for energy_var in [70,100,170,226]:

                existing_ic_instance = DIcMeasurement.objects.filter(
                    Q(energy=energy_var) &
                    Q(measurementid=hlavicka_instance) &
                    Q(ic_id=form.icid)
                ).first()
                print(hlavicka_instance)
                print(existing_ic_instance)
                
                if existing_ic_instance is None:

                    ic_instance = DIcMeasurement(
                    energy = energy_var,
                    measurementid=hlavicka_instance,
                    ic_id = form.icid,
                    response_mu = getattr(form,'ic'+str(energy_var)+'_mu'),
                    response_nc = getattr(form,'ic'+str(energy_var)+'_nc')
                    )
                else:
                # Use the existing instance
                    ic_instance = existing_ic_instance
                print(ic_instance)
                ic_instance.save()

                existing_mlic_instance = DMlicMeasurement.objects.filter(
                    Q(energy=energy_var) &
                    Q(measurementid=hlavicka_instance) &
                    Q(icid=form.icid)
                ).first()
                
                if existing_mlic_instance is None:

                    mlic_instance = DMlicMeasurement(
                    energy = energy_var,
                    measurementid=hlavicka_instance,
                    mlicid = form.mlicid,
                    range = getattr(form,'mlic'+str(energy_var)+'_range')
                    )
                else:
                # Use the existing instance
                    mlic_instance = existing_mlic_instance
                mlic_instance.save()


        #form.delete()

        #return redirect('sucess_url')

        return HttpResponseRedirect('/daily'+str(gtr))
    #datajson = jdumps({'datacheck': datacheck.count()})
    #if submitted
    #print(last)
    return render(request, 'daily_QA/'+str(gtr)+'.html', {'gtr':gtr, 'datacheck': datacheck.count(), 'reload': last})

def validovat(request,gtr):
    
    listbygantry = DailyTestDraft.objects.values().filter(gantry=gtr)#.order_by("-index",)[0]
    last=listbygantry.order_by('-index')[0]
    index = (last['index'])
    form = DailyTest.objects.get(pk=index)
    print("Hi, " + form)

    if request.POST.get('tlacitko')=='Submit':
        print("Now validate")
        #destination_instance = DailyTest()
        #destination_instance.gantry = gantry


    return render(request, 'submitted.html')
 
def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})

def daily_reload(request):
    return render(request, 'daily_QA/daily_reload.html')