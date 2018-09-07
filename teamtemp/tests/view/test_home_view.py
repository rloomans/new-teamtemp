from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from teamtemp import utils
from teamtemp.tests.factories import TeamTemperatureFactory

class HomeViewTestCases(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_homepage_create_teamtemp(self):
        password = utils.random_string(8)
        data = {'survey_type': 'TEAMTEMP', 'new_password': password, 'confirm_password': password}
        response = self.client.post(reverse('home'), data, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'team.html')
