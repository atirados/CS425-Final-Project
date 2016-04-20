from __future__ import unicode_literals

from django.db import models


class JobType(models.Model):
    job_title = models.CharField(max_length=120, default='', blank=True, null=False)
    job_description = models.CharField(max_length=500, default='', blank=True, null=False) 

    
    def __unicode__(self):
        return self.job_title
# Create your models here.
