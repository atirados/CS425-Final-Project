from django.contrib import admin

# Register your models here.
from .forms import ScheduleForm
from .models import Schedule
from Job.models import JobType
from Employee.models import Employee

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "day"]
    #class Meta:
        #model= Schedule
        #model= JobType
    form= ScheduleForm

admin.site.register(Schedule, ScheduleAdmin)

