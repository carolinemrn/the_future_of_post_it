from django.forms import ModelForm
from django import forms

from app.models import Task


class TaskForm(ModelForm):
    description = forms.CharField(max_length=400)
    done = forms.BooleanField(initial=False, widget=forms.CheckboxInput, required=False)

    class Meta:
        model = Task
        fields = ('description', 'done')
