# #You can then create a form for adding new QA tests, and a view to handle the form submission:

# from django import forms
# from .models import QATest

# class QATestForm(forms.ModelForm):
#     class Meta:
#         model = QATest
#         fields = ['patient', 'date', 'test_type', 'result']

# #In this example, we have a qa_test view that handles the form submission for adding new QA tests. 
# #The view first checks if the request method is POST, and if so, validates the form and saves the QA test to the database. 
# #If the request method is not POST, the view returns a blank form.

# #--------------------------------------------------------------------------------------------------------------------------

# #Plan prediction: You can create a form to allow the user to input patient data,and use this data to make plan predictions. 
# #You can create a URL pattern and a view to handle the form submission, and return the plan predictions to the user. 
# #Here's an example:

# #from django import forms
# from .models import Patient

# class PlanPredictionForm(forms.Form):
#     patient = forms.ModelChoiceField(queryset=Patient.objects.all())
#     # other fields for inputting patient data
# #--------------------------------------------------------------------------------------------------------------------------

# from django import forms
# from .models import DailyQATest

# class DailyQATestForm(forms.ModelForm):
#     class Meta:
#         model = DailyQATest
#         exclude = ['user', 'date']

#============================================================================================================================

# forms.py

from django import forms
from .models import QA, Plan


class QAForm(forms.ModelForm):
    class Meta:
        model = QA
        fields = ['room', 'date', 'test_1', 'test_2', 'test_3', 'test_4', 'test_5', 'test_6', 'test_7', 'test_8', 'test_9', 'test_10']


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['image', 'plan_type']