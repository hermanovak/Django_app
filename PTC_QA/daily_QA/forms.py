#NOTE this form isn't necessary if we're making them by hand in html

from django import forms
from django.forms import ModelForm
from .models import DailyTest, DailyTestInput

#Create daily QA form
class DailyTestForm(ModelForm):
    # define the fields to render, inherit from daily.html?
    date_added = forms.DateTimeField(widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'type': 'date'}),required=False)
    #gantry_choices=[(1, "FBTR1"),(2, "GTR2"),(3, "GTR3"),(4, "GTR4")]
    #gantry = forms.IntegerField(widget=forms.Select(choices=gantry_choices))gantry = forms.IntegerField(widget=forms.Select(choices=gantry_choices))
    gantry = forms.IntegerField(required=False)
    visionrt_check = forms.BooleanField(label="Vision RT?",required=False)
    flatpanels_check = forms.BooleanField(label="Flat panely?",required=False)
    dynr = forms.BooleanField(label="DynR?",required=False)
    lasers = forms.BooleanField(label="Lasery x, y, z?",required=False)
    temperature = forms.DecimalField(required=False)
    pressure = forms.DecimalField(required=False)
    kfactor = forms.DecimalField(required=False)

    class Meta:
        model = DailyTest
        #fields = ['date_added', 'visionrt_check', 'flatpanels_check', 'dynr', 'lasers']
        #exclude = ('gantry',)
        #fields = ('') #make a list of required fields
        fields = '__all__'
        

#Create daily QA form
class DailyTestInputForm(ModelForm):
    #index = forms.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    energyID = forms.IntegerField(required=False)
    input1 = forms.DecimalField(max_digits=10, decimal_places=4)  # Field name made lowercase.
    input2 = forms.DecimalField(max_digits=10, decimal_places=4, required=False)  # Field name made lowercase.
    input3 = forms.DecimalField(max_digits=10, decimal_places=4, required=False)  # Field name made lowercase.
    input4 = forms.DecimalField(max_digits=10, decimal_places=4, required=False)  # Field name made lowercase.
    configID = forms.IntegerField(required=False)
    #indexid = forms.ForeignKey(DailyTest, on_delete=forms.CASCADE, null=True) 

    class Meta:
        model = DailyTestInput
        #fields = '__all__'
        exclude = ('indexid',)
