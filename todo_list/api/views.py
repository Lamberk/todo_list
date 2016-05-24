from rest_framework import generics
from rest_framework.response import Response

from todo_list.api.serializers import TaskListCreateSerializer, TaskRtrUpdDestrSerializer
from todo_list.api.models import Task


class TaskListCreate(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of tasks.
    """
    serializer_class = TaskListCreateSerializer

    def list(self, request):
        if not self.request.session.session_key:
            self.request.session['is_login'] = True
        queryset = self.get_queryset()
        serializer = TaskListCreateSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        if not self.request.session.session_key:
            self.request.session['is_login'] = True
        session_key = self.request.session.session_key
        return Task.objects.filter(session_key=session_key)


class TaskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskRtrUpdDestrSerializer

