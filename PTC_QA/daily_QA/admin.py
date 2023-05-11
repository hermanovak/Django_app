from django.contrib import admin
from .models import *

# Register your models here.
#from .models import "table"
#admin.site.register("table")

#class DailyAdmin(admin.ModelAdmin):
#    list_display = ['date_added', 'temperature', 'pressure']

admin.site.register(DailyTest)
                    #, DailyAdmin)