# # This view function will handle the GET and POST requests for the Daily QA Test page. 
# The @login_required decorator ensures that only authenticated users can access this page.

# # The if request.method == 'POST': block will handle the submission of the form. 
# When the form is submitted, the room, description, value1, and value2 fields will be extracted from the POST data 
# and used to create a new QAData object, which will be saved to the database.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import QAData

@login_required
def daily_qa_test(request):
    if request.method == 'POST':
        room = request.POST.get('room')
        for i in range(1, 11):
            description = request.POST.get('description_'+str(i))
            value1 = request.POST.get('value1_'+str(i))
            value2 = request.POST.get('value2_'+str(i))
            QAData.objects.create(room=room, description=description, value1=value1, value2=value2)
    return render(request, 'daily_qa_test.html')

