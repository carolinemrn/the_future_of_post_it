from django.forms import ModelForm
from django import forms

from app.models import PostIt, Task
from the_future_of_post_it import settings


class PostItForm(ModelForm):
    title = forms.CharField(max_length=100)
    tasks = forms.ModelMultipleChoiceField(queryset=Task.objects.all(), required=True)
    createdAt = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    toDoFor = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model = PostIt
        fields = ('title', 'tasks', 'createdAt', 'toDoFor')

