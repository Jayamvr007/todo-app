from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'ADD New Task....'}))
    class Meta:
        model=task
        fields='__all__'