from django.urls import reverse
from django.test import TestCase
from rest_framework import status


class AboutViewTestCases(TestCase):
    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'about.html')
        self.assertGreater(len(response.content), 0)
