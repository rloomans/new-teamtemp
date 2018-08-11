import datetime

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from django.utils.timezone import utc
from rest_framework import status

from teamtemp.tests.view.admin_only_view_testcase import AdminOnlyViewTestCase


class SuperViewTestCases(AdminOnlyViewTestCase):
    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create(
            id=100,
            password='sha1$995a3$6011485ea3834267d719b4c801409b8b1ddd0158',
            last_login=datetime.datetime(
                2007,
                5,
                30,
                13,
                20,
                10,
                tzinfo=utc),
            is_superuser=True,
            username='super',
            first_name='Super',
            last_name='User',
            email='super@example.com',
            is_staff=True,
            is_active=True,
            date_joined=datetime.datetime(
                2007,
                5,
                30,
                13,
                20,
                10,
                tzinfo=utc))

    def test_super_view(self):
        self.client.force_login(self.superuser)
        super_url = reverse('super', kwargs={'survey_id': self.teamtemp.id})
        response = self.client.get(super_url, follow=True)
        self.assertIsNotPasswordForm(response)
        self.assertIsAdminForm(response)

    def test_super_view_no_djauth(self):
        self.setUpAdmin()
        super_url = reverse('super', kwargs={'survey_id': self.teamtemp.id})
        response = self.client.get(super_url, follow=True)
        self.assertRedirects(
            response, expected_url=(
                '/djadmin/login/?next=%s' %
                super_url), status_code=status.HTTP_302_FOUND)

    def test_super_view_no_auth(self):
        super_url = reverse('super', kwargs={'survey_id': self.teamtemp.id})
        response = self.client.get(super_url, follow=True)
        self.assertRedirects(
            response, expected_url=(
                '/djadmin/login/?next=%s' %
                super_url), status_code=status.HTTP_302_FOUND)
