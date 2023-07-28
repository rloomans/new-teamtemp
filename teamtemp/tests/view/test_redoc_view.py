from django.urls import reverse
from django.test import TestCase
from rest_framework import status


class RedocViewTestCases(TestCase):
    def test_redoc_view(self):
        response = self.client.get(reverse('redoc'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.content), 0)
