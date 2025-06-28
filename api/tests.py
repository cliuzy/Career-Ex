from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Task

class TaskAPITests(APITestCase):
    def setUp(self):
        # Create a sample task for testing
        self.task = Task.objects.create(
            title="Initial test task",
            completed=False
        )
        self.list_url = reverse('task-list-create')
        self.detail_url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.pk})

    def test_create_task(self):
        """
        Ensure we can create a new task
        """
        data = {
            'title': 'New test task',
            'completed': True
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=2).title, 'New test task')

    def test_list_tasks(self):
        """
        Ensure we can retrieve the list of tasks
        """
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Initial test task')

    def test_retrieve_task(self):
        """
        Ensure we can retrieve a single task
        """
        response = self.client.get(self.detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Initial test task')

    def test_update_task(self):
        """
        Ensure we can update a task
        """
        data = {
            'title': 'Updated test task',
            'completed': True
        }
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated test task')
        self.assertEqual(self.task.completed, True)

    def test_partial_update_task(self):
        """
        Ensure we can partially update a task
        """
        data = {'completed': True}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.completed, True)

    def test_delete_task(self):
        """
        Ensure we can delete a task
        """
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)