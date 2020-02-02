from django.forms import ModelForm

from django import forms
from app.models import PostitTask


class PostitTaskForm(ModelForm):
    done = forms.BooleanField(widget=forms.CheckboxInput(attrs={'onclick': 'this.form.submit()', 'class': 'check_box',
                                                                'id': 'task_pi', 'name': 'task_pi'}),
                              required=False)

    class Meta:
        model = PostitTask
        fields = ('done',)
