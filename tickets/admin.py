from django.contrib import admin

# Register your models here.
from .models import PurchaseTicket
from .forms import PurchaseTicketForm

class PurchaseTicketAdmin(admin.ModelAdmin):
	list_display = ["__str__","timestamp"]
	form = PurchaseTicketForm


admin.site.register(PurchaseTicket, PurchaseTicketAdmin)