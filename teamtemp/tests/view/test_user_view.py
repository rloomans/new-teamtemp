from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from teamtemp import responses
from teamtemp.responses import utils
from teamtemp.tests.factories import UserFactory


class UserViewTestCases(TestCase):
    def test_user_missing_view(self):
        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'user.html')

    def test_user_not_in_db_view(self):
        session = self.client.session
        session[responses.USER_ID_KEY] = utils.random_string(32)
        session.save()

        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'user.html')

    def test_user_found_view(self):
        user = UserFactory()

        session = self.client.session
        session[responses.USER_ID_KEY] = user.id
        session.save()

        response = self.client.get(reverse('user'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'user.html')
