from django import forms
from . import models

class CreateEntry(forms.ModelForm):
    class Meta:
        model = models.Entry
        fields = ['title', 'body', 'url', 'pic']