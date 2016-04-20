from django.shortcuts import render
from movies.models import Movie
# from django.http import HttpResponse

# Create your views here.


def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the
    # template!

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    movie_list = Movie.objects.order_by('title')
    context_dict = {'movies': movie_list}
    return render(request, 'movies/index.html', context_dict)
