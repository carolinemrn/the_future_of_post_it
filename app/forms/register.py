from django.contrib.auth.models import User
from django.forms import models


class RegisterForm(models.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']