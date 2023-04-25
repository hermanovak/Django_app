 #QAtests:You can create a Django model to represent the QAtests, and create a form to allow the user to add new QA test results to the database. 
 #The form can be accessed via a URL pattern in your app's `urls.py` file, and the form submission can be handled by a view that saves the new QA test result to the database. 
 #Here's an example:

# from django.db import models
# from django.contrib.auth.models import User

# class QATest(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     date = models.DateField()
#     test_type = models.CharField(max_length=50)
#     result = models.CharField(max_length=50)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#In this example, we have a `QATest` model that represents a QA test. 
#The model has a foreign key to the `Patient` model, and a `user` foreign key to the `User` model, to associate the QA test with a particular user.

#============================================================================================================================

from django.contrib.auth.models import User
from django.db import models


class QA(models.Model):
    ROOM_CHOICES = [
        ('Room 1', 'Room 1'),
        ('Room 2', 'Room 2'),
        ('Room 3', 'Room 3'),
        ('Room 4', 'Room 4')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.CharField(max_length=10, choices=ROOM_CHOICES)
    date = models.DateField()
    test_1 = models.CharField(max_length=100)
    test_2 = models.CharField(max_length=100)
    test_3 = models.CharField(max_length=100)
    test_4 = models.CharField(max_length=100)
    test_5 = models.CharField(max_length=100)
    test_6 = models.CharField(max_length=100)
    test_7 = models.CharField(max_length=100)
    test_8 = models.CharField(max_length=100)
    test_9 = models.CharField(max_length=100)
    test_10 = models.CharField(max_length=100)


class Plan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    plan_type = models.CharField(max_length=100)