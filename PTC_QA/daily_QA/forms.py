#NOTE this form isn't necessary if we're making them by hand in html

from django import forms
from django.forms import ModelForm
from .models import DailyTest, DLynxReference

#Create daily QA form
class DailyTestForm(ModelForm):
    # define the fields to render, inherit from daily.html?
    date_added = forms.DateTimeField(widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'type': 'date'}))
    gantry_choices=[(1, "FBTR1"),(2, "GTR2"),(3, "GTR3"),(4, "GTR4")]
    gantry = forms.IntegerField(widget=forms.Select(choices=gantry_choices))
    visionrt_check = forms.BooleanField(label="Vision RT?")
    flatpanels_check = forms.BooleanField(label="Flat panely?")
    dynr = forms.BooleanField(label="DynR?")
    lasers = forms.BooleanField(label="Lasery x, y, z?")
    temperature = forms.DecimalField()
    pressure = forms.DecimalField()

    class Meta:
        model = DailyTest
        fields = "__all__"
        #fields = ('') #make a list of required fields
        

#Create daily QA form
class DLynxReferenceForm(ModelForm):
    # define the fields to render, inherit from daily.html?
    #lynx = forms.IntegerField(widget=forms.Select(choices=index.objects.all()))

    class Meta:
        model = DLynxReference
        fields = "__all__"
        #fields = ('') #make a list of required fields
        