from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import FormView, ListView

from app.forms.login import LoginForm
from app.forms.postit import PostItForm
from app.forms.register import RegisterForm
from app.models import Person, PostIt, Task


class IndexView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'index.html'
    model = PostIt

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = 'Tout les post-it'
        return result


class LogView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse('app_index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        pw = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=pw)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.get_success_url())
        return render(self.request, self.template_name)


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('app_index')

    def form_valid(self, form):
        if form.cleaned_data['password1'] != form.cleaned_data['password2']:
            return False
        user = User.objects.create_user(username=form.cleaned_data['username'],
                                        email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password1'],
                                        )
        user.save()
        person = Person(user=user)
        person.save()
        return HttpResponseRedirect(self.get_success_url())


class PostItView(FormView):
    template_name = 'post-it.html'
    form_class = PostItForm

    def get_success_url(self):
        return reverse('app_index')

    def form_valid(self, form):
        task = Task.objects.create(description=form.cleaned_data['task'])
        if not task:
            return HttpResponseRedirect('EEEEEEEEEEEE')
        postIt = PostIt.objects.create(title=form.cleaned_data['title'],
                                       createdAt=form.cleaned_data['createdAt'],
                                       toDoFor=form.cleaned_data['toDoFor'])
        postIt.tasks.add(task)
        return HttpResponseRedirect(self.get_success_url())


class LogOutView(LogoutView):
    next_page = '/login'
