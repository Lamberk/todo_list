from todo_list.api.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'session_key', 'title', 'text')


class TaskRtrUpdDestrSerializer(TaskSerializer):

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.text = data.get('text', instance.text)
        instance.save()
        return instance


class TaskListCreateSerializer(TaskSerializer):

    def create(self, data):
        session_key = self.context.get('request').session.session_key
        data['session_key'] = session_key
        return Task.objects.create(**data)
