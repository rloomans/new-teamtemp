from teamtemp.tests.view.admin_only_view_testcase import AdminOnlyViewTestCase


class AdminViewTestCases(AdminOnlyViewTestCase):
    def test_no_admin_no_team_view(self):
        response = self.client.get(self.admin_url(), follow=True)
        self.assertDoesLoginRedirect(response, redirect_to=self.admin_url())
        self.assertIsPasswordForm(response)

    def test_admin_no_team_view(self):
        self.setUpAdmin()
        response = self.client.get(self.admin_url(), follow=True)
        self.assertIsNotPasswordForm(response)
        self.assertIsAdminForm(response)

    def test_no_admin_team_view(self):
        admin_url = self.admin_url(for_team=True)
        response = self.client.get(admin_url, follow=True)
        self.assertDoesLoginRedirect(response, redirect_to=admin_url)
        self.assertIsPasswordForm(response)

    def test_admin_team_view(self):
        self.setUpAdmin()
        response = self.client.get(self.admin_url(for_team=True), follow=True)
        self.assertIsNotPasswordForm(response)
        self.assertIsAdminForm(response, for_team=True)
