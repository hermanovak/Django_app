from django.shortcuts import render, redirect
from .models import DailyTest, DailyTestInput, DLynxMeasurement, DailyTestDraft, DIcMeasurement, DMlicMeasurement #must import all needed tables
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q
from django.urls import reverse

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
        form = DailyTestDraft.objects.create(gantry=gtr, date_added = timezone.now()) 
          
    #identify record's index
    listbygantry = DailyTestDraft.objects.values().filter(gantry=gtr)#.order_by("-index",)[0]
    last=listbygantry.order_by('-index')[0]
    index = (last['index'])
    form = DailyTestDraft.objects.get(pk=index)

    if request.method == "POST" and request.POST.get('tlacitko')!='Submit':   

        fields_mapping = {
            'temperature': 'Temp',
            'pressure': 'Pres',
            'kfactor': 'kfactor',
            'laserx': 'X',
            'lasery': 'Y',
            'laserz': 'Z',
            'flatpanels_check': 'FlatPanels',
            'visionrt_check': 'VisionRT',
            'dynr': 'DynR',
            'lynxid': 'LynxID',
            'lynx70_95': 'L7095',
            'lynx70_99': 'L7099',
            'lynx70_max': 'L70max',
            'lynx70_avg': 'L70avg',
            'lynx115_95': 'L11595',
            'lynx115_99': 'L11599',
            'lynx115_max': 'L115max',
            'lynx115_avg': 'L115avg',
            'lynx145_95': 'L14595',
            'lynx145_99': 'L14599',
            'lynx145_max': 'L145max',
            'lynx145_avg': 'L145avg',
            'lynx226_95': 'L22695',
            'lynx226_99': 'L22699',
            'lynx226_max': 'L226max',
            'lynx226_avg': 'L226avg',
            'icid': 'IcID',
            'ic70_mu': 'K70mu',
            'ic70_nc': 'K70nc',
            'ic100_mu': 'K100mu',
            'ic100_nc': 'K100nc',
            'ic170_mu': 'K170mu',
            'ic170_nc': 'K170nc',
            'ic226_mu': 'K226mu',
            'ic226_nc': 'K226nc',
            'mlicid': 'MlicID',
            'mlic70_range': 'MLIC70',
            'mlic100_range': 'MLIC100',
            'mlic170_range': 'MLIC170',
            'mlic226_range': 'MLIC226',
            # Add more fields here
        }

        # Iterate through the dictionary to update form fields
        for field_name, request_param in fields_mapping.items():
            param_value = request.POST.get(request_param)
            if param_value is not None:
                if param_value == 'true':
                    setattr(form, field_name, 1)
                elif param_value == 'false':
                    setattr(form, field_name, 0)
                else:
                    setattr(form, field_name, param_value)
            
        form.save()
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
            gantry=form.gantry
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
                Q(measurementid=hlavicka_instance)
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

            existing_mlic_instance = DMlicMeasurement.objects.filter(
                Q(energy=energy_var) &
                Q(measurementid=hlavicka_instance)
            ).first()
            
            if existing_mlic_instance is None: # && mlic enabled
                mlic_instance = DMlicMeasurement(
                energy = energy_var,
                measurementid=hlavicka_instance,
                mlicid = form.mlicid,
                range = getattr(form,'mlic'+str(energy_var)+'_range')
                )
                mlic_instance.save()
            
            #else:
            # Use the existing instance
                #mlic_instance = existing_mlic_instance
            

            existing_ic_instance = DIcMeasurement.objects.filter(
                Q(energy=energy_var) &
                Q(measurementid=hlavicka_instance)
            ).first()

            
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
            ic_instance.save()

        #print("Submitted")
        return HttpResponseRedirect(reverse('daily_QA:submitted', args=(gtr,)))
        
        #form.delete()
        #return redirect('sucess_url')

    return render(request, 'daily_QA/'+str(gtr)+'.html', {'gtr':gtr, 'datacheck': datacheck.count(), 'reload': last})

def submitted(request,gtr):
    return render(request, 'daily_QA/submitted.html', {'gtr': gtr})
 
def success2(request,gtr):
    return render(request, 'daily_QA/success2.html', {'gtr': gtr})

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})

def daily_reload(request):
    return render(request, 'daily_QA/daily_reload.html')