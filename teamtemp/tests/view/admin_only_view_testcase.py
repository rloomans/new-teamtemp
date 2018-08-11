from future import standard_library
standard_library.install_aliases()

from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from teamtemp import responses
from teamtemp.tests.factories import TeamTemperatureFactory, TeamFactory


class AdminOnlyViewTestCase(TestCase):
    def setUp(self):
        self.teamtemp = TeamTemperatureFactory()
        self.team = TeamFactory(request=self.teamtemp)

    def admin_url(self, for_team=False):
        if for_team:
            return reverse(
                'admin',
                kwargs={
                    'survey_id': self.teamtemp.id,
                    'team_name': self.team.team_name})
        else:
            return reverse('admin', kwargs={'survey_id': self.teamtemp.id})

    def login_url(self, redirect_to=None):
        if not redirect_to:
            redirect_to = self.admin_url()

        return reverse(
            'login',
            kwargs={
                'survey_id': self.teamtemp.id,
                'redirect_to': redirect_to})

    def assertIsPasswordForm(self, response):
        self.assertContains(response, 'Enter the admin password')
        self.assertTemplateUsed(response, 'password.html')

    def assertIsNotPasswordForm(self, response):
        self.assertNotContains(response, 'Enter the admin password')
        self.assertTemplateNotUsed(response, 'password.html')

    def assertIsAdminForm(self, response, for_team=False):
        if for_team:
            self.assertContains(
                response, "Admin %s %s" %
                (self.teamtemp.id, self.team.team_name))
        else:
            self.assertContains(response, "Admin %s" % self.teamtemp.id)
        self.assertTemplateUsed(response, 'results.html')

    def assertDoesLoginRedirect(
            self,
            response,
            expected_url=None,
            redirect_to=None):
        if not expected_url:
            expected_url = self.login_url(redirect_to=redirect_to)

        self.assertRedirects(
            response,
            expected_url=expected_url,
            status_code=status.HTTP_302_FOUND)

    def setUpAdmin(self):
        session = self.client.session
        session[responses.ADMIN_KEY] = [self.teamtemp.id]
        session.save()
