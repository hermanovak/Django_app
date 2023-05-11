#NOTE this form isn't necessary if we're making them by hand in html

from django import forms
from django.forms import ModelForm
from .models import DailyTest, DailyTestInput

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
class DailyTestInputForm(ModelForm):
    #index = forms.AutoField(db_column='Index', primary_key=True)  # Field name made lowercase.
    energyID = forms.IntegerField(db_column='energyID')
    input1 = forms.DecimalField(db_column='input1', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    input2 = forms.DecimalField(db_column='input2', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    input3 = forms.DecimalField(db_column='input3', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    input4 = forms.DecimalField(db_column='input4', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    configID = forms.IntegerField(db_column='configID')

    class Meta:
        model = DailyTestInput
        fields = '__all__'
