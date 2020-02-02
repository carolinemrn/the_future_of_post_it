from django.contrib import admin

from app.models import Person, PostIt, Task, PostitTask

admin.site.register(Person)
admin.site.register(PostIt)
admin.site.register(Task)
admin.site.register(PostitTask)