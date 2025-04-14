import json

from django.contrib.auth.models import User
from django.test import TestCase
import pytest

from .models import Categories, Tasks


@pytest.mark.django_db
class TasksTest(TestCase):

    def setUp(self):
        self.url = "/api/v1/"
        self.user = User.objects.create(username="test_user",password="12345qwerty")
        self.client.force_login(user=self.user)
        self.category = Categories.objects.create(category_name="Test Category", created_user_id = self.user.id)
        self.content_type = "application/json"
        self.data_create = {
            "title": "string",
            "content": "string",
            "time": "08:00",
            "category": self.category,
            "repeat_days": "1 2 3",
            "author":self.user
            }
    def test_tasks_create(self):
        response = self.client.post(data=self.data_create,
                                    path=self.url+"tasks/",
                                    content_type=self.content_type)
        self.assertEqual(response.status_code,201)

    def test_tasks_get(self):
        response = self.client.get(path=self.url+"tasks/")
        self.assertEqual(response.status_code, 200)

    def test_tasks_put(self):
        data_changed = {
            "title": "qqqqq",
            "content": "qqqqq",
            "time": "10:00",
            "repeat_days": "",
        }
        task = Tasks.objects.create(**self.data_create)
        response_put = self.client.put(data=data_changed,path=self.url+f"tasks/{task.id}/", content_type=self.content_type)
        self.assertEqual(response_put.status_code, 200)

    def test_tasks_delete(self):
        task = Tasks.objects.create(**self.data_create)
        response = self.client.delete(path=self.url+f"tasks/{task.id}/", content_type=self.content_type)
        self.assertEqual(response.status_code, 204)

