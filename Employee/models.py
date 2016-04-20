from __future__ import unicode_literals

from django.db import models
class Employee(models.Model):
    first_name = models.CharField(max_length=120, default='', blank=False, null=False)
    last_name = models.CharField(max_length=120, default='', blank=False, null=False)
    SSN = models.PositiveIntegerField()
    address = models.CharField(max_length=200, default='', blank=False, null=False)
    phone =models.PositiveIntegerField()
    work_location=models.CharField(max_length=120, default='', blank=False, null=False)
    

    
    def __unicode__(self):
        return self.first_name + ' '+ self.last_name
# Create your models here.
