from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from app.forms.login import LoginForm
from app.forms.postit import PostItForm
from app.forms.postit_task import PostitTaskForm
from app.forms.register import RegisterForm
from app.forms.task import TaskForm
from app.models import Person, PostIt, Task, PostitTask
from django.utils.translation import gettext_lazy as _

from django.core.mail import send_mail


class IndexView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'index.html'
    model = PostIt

    def get_queryset(self):
        if self.request.GET.get('search') is not None:
            return PostIt.objects.filter(user_id=Person.objects.get(user=self.request.user),
                                         title__icontains=self.request.GET.get("search"))
        else:
            return PostIt.objects.filter(user_id=Person.objects.get(user=self.request.user))

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['title'] = _('Title')
        result['user'] = Person.objects.get(user=self.request.user)
        result['form'] = PostitTaskForm()
        return result


class PostitTaskView(FormView):
    template_name = 'index.html'
    model = PostitTask
    form_class = PostitTaskForm

    def get_success_url(self):
        return reverse('app_index')

    def form_valid(self, form):
        input_hidden = self.request.POST.get('task_pi', None)
        input_hidden.split('_')
        task = input_hidden[0]
        postit = input_hidden[2]
        postittask = PostitTask.objects.filter(postit_id=postit).filter(task_id=task)
        if postittask.filter(done=False):
            postittask.update(done=True)
        else:
            postittask.update(done=False)
        return HttpResponseRedirect(self.get_success_url())


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
        postIt = PostIt.objects.create(title=form.cleaned_data['title'],
                                       createdAt=form.cleaned_data['createdAt'],
                                       toDoFor=form.cleaned_data['toDoFor'],
                                       user=Person.objects.get(user=self.request.user))
        tasks = form.cleaned_data['tasks']
        for task in tasks:
            postIt.tasks.add(task)
            PostitTask.objects.create(postit=postIt, task=task, done=False)
        return HttpResponseRedirect(self.get_success_url())


class TaskView(FormView):
    template_name = 'task.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('app_task')

    def form_valid(self, form):
        description = form.cleaned_data['description']
        task = Task(description=description)
        task.save()
        return HttpResponseRedirect(self.get_success_url())


class LogOutView(LogoutView):
    next_page = '/login'


class PostItUpdate(UpdateView):
    template_name = 'post-it-update.html'
    model = PostIt
    form_class = PostItForm

    def get_success_url(self):
        return reverse('app_index')

    def form_valid(self, form):
        tasks = form.cleaned_data['tasks']
        for task in tasks:
            task.save()
        return HttpResponseRedirect(self.get_success_url())


class PostItDelete(DeleteView):
    template_name = 'post-it-delete.html'
    model = PostIt
    form_class = PostItForm

    def get_success_url(self):
        return reverse('app_index')


