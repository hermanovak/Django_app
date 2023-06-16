from django.contrib import admin
#from .models import *
from .models import DailyTestDraft, DailyTestInput, DLynxMeasurement
from .models import DailyTest 

# Register your models here.
#from .models import "table"
#admin.site.register("table")

#class DailyAdmin(admin.ModelAdmin):
#    list_display = ['date_added', 'temperature', 'pressure']
admin.site.register(DailyTestDraft)
admin.site.register(DailyTest)
admin.site.register(DailyTestInput)
admin.site.register(DLynxMeasurement)


                    #, DailyAdmin)