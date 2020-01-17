from django.forms import ModelForm, widgets
from django import forms

from app.models import PostIt
from the_future_of_post_it import settings


class PostItForm(ModelForm):
    title = forms.CharField(max_length=100)
    createdAt = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    toDoFor = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = PostIt
        fields = ('title', 'content', 'createdAt', 'toDoFor')
