
from django import forms
from .models import Subscriber, Newsletter

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']

class NewsletterForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, label='Body')
    class Meta:
        model = Newsletter
        fields = ['title', 'content']
