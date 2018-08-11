from django.urls import reverse

from teamtemp.tests.view.admin_only_view_testcase import AdminOnlyViewTestCase


class AdminViewTestCases(AdminOnlyViewTestCase):
    def test_no_admin_reset_view(self):
        reset_url = reverse('reset', kwargs={'survey_id': self.teamtemp.id})
        response = self.client.get(reset_url, follow=True)
        self.assertDoesLoginRedirect(response, redirect_to=reset_url)
        self.assertIsPasswordForm(response)

    def test_admin_reset_team_view(self):
        self.setUpAdmin()
        response = self.client.get(
            reverse(
                'reset',
                kwargs={
                    'survey_id': self.teamtemp.id}),
            follow=True)
        self.assertIsNotPasswordForm(response)
        self.assertIsAdminForm(response)
