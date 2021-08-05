from django.urls import reverse
from django.test import TestCase
from rest_framework import status

class HealthcheckViewTestCases(TestCase):
    def test_health_check_view(self):
        response = self.client.get(reverse('healthcheck'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertTemplateNotUsed(response, 'index.html')
        self.assertEqual(response.content, b'ok')
        self.assertContains(response, 'ok')
