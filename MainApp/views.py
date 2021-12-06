from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm
from .models import Topic, Entry
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    '''The home page for Learning Log.'''
    return render(request, 'MainApp/index.html')

@login_required
def topics(request):
    topics = Topic.objects.order_by('date_added')

    # the key is the variable used in the template file and the value is the variable used in the view function
    context = {'topics':topics}

    return render(request, 'MainApp/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    entries = topic.entry_set.all()
    context = {'topic':topic, 'entries':entries}

    return render(request, 'MainApp/topic.html', context)

@login_required
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

@login_required
def new_entry(request, topic_id): # need to use the same variable from the URLs file (we use topic_id in the urls.py file)
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm() # loading an empty form if get request
    else:
        form = EntryForm(data=request.POST) # if a post request, get the data from the webpage

        if form.is_valid():
            new_entry = form.save(commit=False) # not ready to write to database quite yet
            new_entry.topic = topic
            new_entry.save()

            return redirect('MainApp:topic', topic_id=topic_id)

    context = {'form': form, 'topic':topic} # dictionary that allows us to pass data into our template
    return render(request, 'MainApp/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    '''Edit an existing entry.'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('MainApp:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'MainApp/edit_entry.html', context)
    