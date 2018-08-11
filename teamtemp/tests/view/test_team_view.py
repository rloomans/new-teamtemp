from django.urls import reverse

from teamtemp.tests.view.admin_only_view_testcase import AdminOnlyViewTestCase


class AdminViewTestCases(AdminOnlyViewTestCase):
    def test_no_admin_existing_team_view(self):
        team_url = reverse(
            'team',
            kwargs={
                'survey_id': self.teamtemp.id,
                'team_name': self.team.team_name})
        response = self.client.get(team_url, follow=True)
        self.assertDoesLoginRedirect(response, redirect_to=team_url)
        self.assertIsPasswordForm(response)

    def test_admin_existing_team_view(self):
        self.setUpAdmin()
        team_url = reverse(
            'team',
            kwargs={
                'survey_id': self.teamtemp.id,
                'team_name': self.team.team_name})
        response = self.client.get(team_url, follow=True)
        self.assertIsNotPasswordForm(response)
        self.assertTemplateUsed(response, 'team.html')
