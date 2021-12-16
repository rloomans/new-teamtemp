from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory

from teamtemp import responses
from teamtemp.responses import USER_ID_KEY


class UserIdTestCases(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.request = RequestFactory().get('/test')

        """Annotate a request object with a session"""
        middleware = SessionMiddleware(self.request)
        middleware.process_request(self.request)
        self.request.session.save()

    def test_get_user_id(self):
        user_id = 'kjhsdafA'

        self.request.session = {USER_ID_KEY: user_id}

        self.assertEqual(responses.get_userid(self.request), user_id)

    def test_set_user_id(self):
        user_id = 'Aasdfa'

        self.assertEqual(responses.set_userid(self.request, user_id), user_id)
        self.assertEqual(responses.get_userid(self.request), user_id)

    def test_create_user_id(self):
        user_id = responses.create_userid(self.request)

        self.assertEqual(user_id, responses.get_userid(self.request))

    def test_is_admin(self):
        self.assertEqual(len(responses.get_admin_for_surveys(self.request)), 0)

        survey_ids = ['test1', 'test2', 'test3']
        for survey_id in survey_ids:
            self.assertFalse(
                responses.is_admin_for_survey(
                    self.request, survey_id))

            responses.add_admin_for_survey(self.request, survey_id)

            self.assertTrue(
                responses.is_admin_for_survey(
                    self.request, survey_id))

        self.assertEqual(
            len(responses.get_admin_for_surveys(self.request)), len(survey_ids))
