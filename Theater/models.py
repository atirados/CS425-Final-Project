from __future__ import unicode_literals

from django.db import models


class Theater(models.Model):
    # theater_ID=models.SmallIntegerField(default=1, null=False)
    theater_name = models.CharField(
        max_length=120, default='', blank=True, null=False)
    address = models.CharField(
        max_length=120, default='', blank=True, null=False)
# Create your models here.

    def __unicode__(self):
        return self.theater_name