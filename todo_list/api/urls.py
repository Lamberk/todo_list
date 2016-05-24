from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from todo_list.api.views import TaskRetrieveUpdateDestroy, TaskListCreate

urlpatterns = [
    url(r'^tasks/(?P<pk>\d+)/$', TaskRetrieveUpdateDestroy.as_view(), name='task-retrieve-update'),
    url(r'^tasks', TaskListCreate.as_view(), name='task-list-create'),
]
