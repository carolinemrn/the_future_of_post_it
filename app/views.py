from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from app.forms.register import RegisterForm
from app.models import Person


class IndexView(TemplateView):
    template_name = 'index.html'
    model = Person


class LogView(LoginView):
    template_name = 'login.html'


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('app_login')

    def form_valid(self, form):
        user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
        person = Person.objects.create(user=user)
        return HttpResponseRedirect(self.get_success_url())