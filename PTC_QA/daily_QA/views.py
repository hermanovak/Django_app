from django.shortcuts import render

def home(request):
    return render(request, 'daily_QA/home.html', {})


def daily(request):
    return render(request, 'daily_QA/daily.html', {})

def weekly(request):
    return render(request, 'daily_QA/weekly.html', {})

def monthly(request):
    return render(request, 'daily_QA/monthly.html', {})