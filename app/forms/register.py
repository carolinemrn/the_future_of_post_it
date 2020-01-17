from django.contrib.auth.models import User
from django.forms import models, forms, widgets, ModelForm
from django import forms

from app.models import Person


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=200, min_length=4,
                               widget=widgets.TextInput)
    email = forms.EmailField(max_length=200, min_length=4,
                             widget=widgets.TextInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(max_length=200, min_length=4,    widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=200, min_length=4, widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalnum():
            self.add_error('username', 'Only alphanum chars allowed !')
            return None
        return username

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            self.add_error('password2', 'Passwords are different !')
        return super().clean()