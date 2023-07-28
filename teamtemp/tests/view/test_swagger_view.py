from django.urls import reverse
from django.test import TestCase
from rest_framework import status


class SwaggerViewTestCases(TestCase):
    def test_swagger_view(self):
        response = self.client.get(reverse('swagger-ui'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.content), 0)
