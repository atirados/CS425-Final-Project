from __future__ import unicode_literals

from django.db import models

# Create your models here.

#MOVIES = ('The Martian', 'Bridge of Spies', 'The Last Witch Hunter')


class PurchaseTicket(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120)
	cc_number = models.CharField(max_length=16)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

def __str__(self): #__unicode__
	return str(self.email) 