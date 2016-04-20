from django import forms
from .models import Schedule
from Job.models import JobType
from Employee.models import Employee
from Theater.models import Theater

class ScheduleForm(forms.ModelForm):
    employee_ID= forms.ModelMultipleChoiceField(queryset=Employee.objects.all())
    job_Type = forms.ModelMultipleChoiceField(queryset=JobType.objects.all())
    work_Location = forms.ModelMultipleChoiceField(queryset=Theater.objects.all())
   
def clean(self):
    
    clean_data=self.cleaned_data
    Employee_ID= cleaned_data.get('employee_ID')
    location = cleaned_data.get('work_Location')
    
    matching_employee=Employee.objects.filter()
    if matching_employee.exist():
        matching_location=Theater.objects.filter()
        
    else:
        return self.cleaned_data
   
    class Meta:
        model= Schedule
        exclude = ('employee_ID',)
        #code
    