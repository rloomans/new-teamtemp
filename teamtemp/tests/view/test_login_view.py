from teamtemp.tests.view.admin_only_view_testcase import AdminOnlyViewTestCase


class LoginViewTestCases(AdminOnlyViewTestCase):
    def test_not_loggedin_view(self):
        response = self.client.get(self.login_url(), follow=True)
        self.assertIsPasswordForm(response)

    def test_loggedin_view(self):
        self.setUpAdmin()
        response = self.client.get(self.login_url(), follow=True)
        self.assertDoesLoginRedirect(response, expected_url=self.admin_url())
        self.assertIsNotPasswordForm(response)
        self.assertIsAdminForm(response)
