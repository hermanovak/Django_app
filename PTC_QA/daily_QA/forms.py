from django import forms
from django.forms import ModelForm
from .models import DailyTest

#Create daily QA form
class DailyTestForm(ModelForm):
    class Meta:
        model = DailyTest
        fields = "__all__"
        #fields = ('') #make a list of required fields
        