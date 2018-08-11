from django.urls import reverse
from django.test import TestCase
from rest_framework import status


class HomeViewTestCases(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
