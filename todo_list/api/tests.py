from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo_list.api.models import Task


class TaskTestCase(APITestCase):
    def test_task(self):
        url = reverse('task-list-create')
        data = {'title': 'Test title', 'text': 'Test text'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)

        response = self.client.get('/api/tasks/')
        self.assertEqual(len(list(response)), 1)

        self.assertEqual(Task.objects.get().title, 'Test title')
        self.assertEqual(Task.objects.get().text, 'Test text')

        pk = Task.objects.get().id
        data = {'title': 'New test title', 'text': 'New test text'}
        response = self.client.put('/api/tasks/{}/'.format(pk), data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'New test title')
        self.assertEqual(Task.objects.get().text, 'New test text')

        response = self.client.delete('/api/tasks/{}/'.format(Task.objects.get().id))
        self.assertEqual(Task.objects.count(), 0)




