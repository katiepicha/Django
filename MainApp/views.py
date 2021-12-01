from django.shortcuts import render, redirect
from .forms import TopicForm
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

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.all()
    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm() # loading an empty form if get request
    else:
        form = TopicForm(data=request.POST) # if a post request, get the data from the webpage

        if form.is_valid():
            form.save()

            return redirect('MainApp:topics')

    context = {'form': form} # dictionary that allows us to pass data into our template
    return render(request, 'MainApp/new_topic.html', context)