from django.contrib import admin

from app.models import Person, PostIt, Task, PostItTask


class PostItTaskInlineAdmin(admin.StackedInline):
    model = PostItTask
    extra = 0


class PostItAdmin(admin.ModelAdmin):
    inlines = (PostItTaskInlineAdmin,)


admin.site.register(Person)
admin.site.register(PostIt, PostItAdmin)
admin.site.register(Task)
admin.site.register(PostItTask)
