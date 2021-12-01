from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''} # add whatever label you want into the empty quotation marks

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''} # add whatever label you want into the empty quotation marks
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} # widgets are an HTML form element - text area will be 80 columns wide
        
