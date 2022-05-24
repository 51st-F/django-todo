from dataclasses import field
from django import forms
from django.forms import ModelForm

from .models import *

class TodoForm(forms.ModelForm):
    class Meta:
        model = todo_item
        fields = '__all__'