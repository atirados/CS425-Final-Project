from django.shortcuts import render
#from .models import PurchaseTicket
from .forms import PurchaseTicketForm
from Theater.models import Theater

# Create your views here.
def home(request):
	title = "Purchase Movie Tickets"

	form = PurchaseTicketForm(request.POST or None)
	
	context = {
		"title": title,
		"form": form	
	}
	
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		print instance.email
		print instance.timestamp
		context = {
			"title": "Thank You! Your purchase has been made."
		}

	return render(request, "tickets/home.html", context) 


def theaters(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the
    # template!

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    theater_list = Theater.objects.order_by('theater_name')
    context_dict = {'theaters': theater_list}
    return render(request, 'tickets/theaters.html', context_dict)