from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} # add whatever label you want into the empty quotation marks