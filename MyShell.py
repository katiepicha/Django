# allows us to examine the data programmatically through an interactive terminal session called the Django shell

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all() # No SQL is dot notation - exactly like doing a SELECT * in SQL, 

for topic in topics:
    print(topic.id)
    print(topic) # can use topic or topic.text because we defined the string function
    print(topic.date_added)


t = Topic.objects.get(id=1) # get() allows us to examine any attributes the object has
print(t)

# Since we defined topic as a foreignkey attribute in the Entry model, Django can use this relationship to access the entries for any topic
entries = t.entry_set.all() # To get data through a foreign key relationship, you use the lowercase name of the related model 
# followed by an underscore and the word set 

for e in entries:
    print(e)
