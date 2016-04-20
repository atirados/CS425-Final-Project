from django import forms

from .models import PurchaseTicket

class PurchaseTicketForm(forms.ModelForm):
	class Meta:
		model = PurchaseTicket
		fields = ['full_name','email', 'cc_number']