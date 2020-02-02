from datetime import date

from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_DEFAULT

from the_future_of_post_it import settings


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{str(self.user)}'


class Task(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True, default='(no task)')

    def __str__(self):
        return self.description if self.description is not None else '? ?'


class PostIt(models.Model):
    title = models.CharField(null=False, blank=False, default="Titre", max_length=100)
    createdAt = models.DateField(default=date.today)
    toDoFor = models.DateField(null=False, blank=False, default=date.today)
    tasks = models.ManyToManyField(Task)
    user = models.ForeignKey(Person, on_delete=models.CASCADE, null=None, default=None)

    def __str__(self):
        return f'{str(self.title)}'

    def get_postittask(self):
        return PostitTask.objects.filter(postit_id=self.id)


class PostitTask(models.Model):
    postit = models.ForeignKey(PostIt, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
