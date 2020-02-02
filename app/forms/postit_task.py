from django.forms import ModelForm, TextInput

from django import forms
from django.urls import reverse
from app.models import PostitTask


# def submit(self):
#     input_hidden = self.cleaned_data['task_pi']
#     input_hidden.split('_')
#     task = input_hidden[0]
#     postit = input_hidden[1]
#     postittask = PostitTask.objects.filter(postit=postit, task=task)
#     if postittask:
#         postittask.done.set(True)
#     return reverse('app_index')


class PostitTaskForm(ModelForm):
    done = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick': 'this.form.submit()', 'class': 'check_box'}),
                              required=False)

    class Meta:
        model = PostitTask
        fields = ('done',)
