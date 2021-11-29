from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    '''The home page for Learning Log.'''
    return render(request, 'MainApp/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')

    # the key is the variable used in the template file and the value is the variable used in the view function
    context = {'topics':topics}

    return render(request, 'MainApp/topics.html', context)