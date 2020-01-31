"""the_future_of_post_it URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from app.views import IndexView, LogView, RegisterView, PostItView, LogOutView, TaskView, PostItUpdate, PostItDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='app_index'),
    path('login/', LogView.as_view(), name='app_login'),
    path('register/', RegisterView.as_view(), name='app_register'),
    path('add-postit/', PostItView.as_view(), name='app_postit'),
    path('logout/', LogOutView.as_view(), name='app_logout'),
    path('add-task/', TaskView.as_view(), name='app_task'),
    path('update-postit/<int:pk>', PostItUpdate.as_view(), name='app_update'),
    path('delete-postit/<int:pk>', PostItDelete.as_view(), name='app_delete'),
]

