from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django import forms

from app.models import Person


class LoginForm(ModelForm):
    username = forms.CharField(max_length=200, min_length=4,
                               widget=widgets.TextInput)
    password = forms.CharField(max_length=200, min_length=4, widget=widgets.PasswordInput)

    class Meta:
        model = Person
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    # def clean(self):
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']
    #     if not User.objects.filter(username=username, password=password).exists():
    #         self.add_error('username', "Le pseudo ou le mot de passe n'existent pas!")
    #     return username

