from django.shortcuts import render

def home(request):
    return render(request, 'daily_QA/home.html', {})


def daily(request):
    #Lasers
    lasers=0
    laserx = 0 #BooleanField("Laser x axis: ")
    lasery = 0 #BooleanField("| Laser y axis: ")
    laserz = 0 #BooleanField("| Laser z axis: ")
    MLICused=False #z html

    if form.laserx.data == True: laserx = 1
    if form.lasery.data == True: lasery = 2
    if form.laserz.data == True: laserz = 4
    lasers = laserx + lasery + laserz

    #Temperature and Pressure
    temperature=0
    pressure=0

    temperature = form.temperature.data
    temperatureK = temperature + 273.15
    pressure = form.pressure.data

    #Coefficients
    Ktp = temperatureK/((273,15+20)*1013/pressure)
    Ksat = 0 #ziskat z databaze
    Kpol = 0 #ziskat z databaze
    Kqq = 0 #ziskat z databaze

    #Lynx data
    lynx_1_115 = 0 #mozna prejmenovat, ziskat z html
    lynx_2_115 = 0 #mozna prejmenovat, ziskat z html
    lynx_3_115 = 0 #mozna prejmenovat, ziskat z html
    lynx_4_115 = 0 #mozna prejmenovat, ziskat z html

    lynx_1_145 = 0 #mozna prejmenovat, ziskat z html
    lynx_2_145 = 0 #mozna prejmenovat, ziskat z html
    lynx_3_145 = 0 #mozna prejmenovat, ziskat z html
    lynx_4_145 = 0 #mozna prejmenovat, ziskat z html

    lynx_1_226 = 0 #mozna prejmenovat, ziskat z html
    lynx_2_226 = 0 #mozna prejmenovat, ziskat z html
    lynx_3_226 = 0 #mozna prejmenovat, ziskat z html
    lynx_4_226 = 0 #mozna prejmenovat, ziskat z html

    #IC
    ic_100 = 0 #mozna prejmenovat, ziskat z html
    ic_170 = 0 #mozna prejmenovat, ziskat z html
    ic_226 = 0 #mozna prejmenovat, ziskat z html

    ic2_100 = 0 #mozna prejmenovat, ziskat z html
    ic2_170 = 0 #mozna prejmenovat, ziskat z html
    ic2_226 = 0 #mozna prejmenovat, ziskat z html

    #MLIC
    if MLICused==True: 
        mlic_100 = 0 #mozna prejmenovat, ziskat z html
        mlic_170 = 0 #mozna prejmenovat, ziskat z html
        mlic_226 = 0 #mozna prejmenovat, ziskat z html

        #change

    return render(request, 'daily_QA/daily.html', {
        "lasers": lasers, 
         "temperature": temperature,
         "pressure": pressure, 
         "Ktp": Ktp, 

    })

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})