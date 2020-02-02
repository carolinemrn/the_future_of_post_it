from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand, CommandError
from django.urls import reverse

from app.models import PostIt, Person, PostitTask, Task


class Command(BaseCommand):

    def handle(self, *args, **options):
        global message, email, mail
        everyone = PostIt.objects.values('user_id').distinct()
        for user in everyone:
            person_id = user['user_id']
            user_id = Person.objects.filter(id=person_id).values('user_id')
            for id in user_id:
                user_user_id = id['user_id']
                emails = User.objects.filter(id=user_user_id).values('email', 'username')
                message = "Il vous reste quelques jours pour terminer ces post-it : <ul>"
                for email in emails:
                    mail = email['email']
                    now_date = datetime.now()
                    posts = PostIt.objects.filter(user_id=person_id).filter(toDoFor__gt=now_date)
                    for post in posts:
                        message += "<li> " + post.title + "<ul>"
                        tasks = PostitTask.objects.filter(postit_id=post.id).filter(done=False).values('task_id')
                        message += "Tâches non complétées :"
                        for task in tasks:
                            task_id = task['task_id']
                            undone_tasks = Task.objects.filter(id=task_id).values('description')
                            for undone_task in undone_tasks:
                                task_task = undone_task['description']

                                message += "<li>" + task_task + "</li>"
                        message += "</ul>"
                message += "</li></ul><br><br> Rendez-vous sur la plateforme pour voir le détail : <a href='http://127.0.0.1:8000/'>ICI</a>"
                email_sent = EmailMessage(
                    email['username'] + " : n'oubliez pas vos post-it !",
                    message,
                    'c.marin@labeteabiere.fr',
                    [mail]
                )
                email_sent.content_subtype = "html"  # this is the crucial part
                email_sent.send()
