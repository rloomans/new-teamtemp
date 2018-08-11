from django.urls import reverse
from django.test import TestCase
from rest_framework import status


class RobotsTxtViewTestCases(TestCase):
    def test_robots_txt_view(self):
        response = self.client.get(reverse('robots_txt'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'text/plain')
        self.assertEqual(response['Cache-Control'], 'public, max-age=86400')
        self.assertTemplateNotUsed(response, 'index.html')
        self.assertGreater(len(response.content), 0)
        self.assertContains(response, 'User-agent:')
        self.assertContains(response, 'Disallow:')
