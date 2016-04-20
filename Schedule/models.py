from __future__ import unicode_literals
from django import forms
from django.db import models
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
     
class Schedule(models.Model):
    MONDAY ='MON'
    TUESDAY = 'TUE'
    WEDNESDAY= 'WED'
    THURSDAY = 'THU'
    FRIDAY ='FRI'
    SATURDAY='SAT'
    SUNDAY= 'SUN'
    DAY_CHOICES =(
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )
    
    #wide_range= range(7, 24, 1)
    #WIND_SPEED_CHOICE =[(i,i) for i in wide_range]
        
    employee_ID = models.CharField(max_length=120, default='', blank=True, null=False)
    day=models.CharField(max_length=7, choices=DAY_CHOICES)
    start_Time =models.IntegerField(validators=[MinValueValidator(7), MaxValueValidator(23)], blank=True)
    end_Time =models.IntegerField(validators=[MinValueValidator(8), MaxValueValidator(23)], blank=True)
    #end_Time =models.CharField(max_length=3, default='9', choices=WIND_SPEED_CHOICE)
    
    def __unicode__(self):
        return self.day
# Create your models here.
