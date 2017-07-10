from django.test import TestCase

from teamtemp.responses.forms import CreateSurveyForm


class CreateSurveyFormTestCases(TestCase):
    def test_empty_create_survey_form(self):
        form_data = {}
        form = CreateSurveyForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_create_survey_form(self):
        form_data = {
            'new_password': 'test',
            'confirm_password': 'test',
        }
        form = CreateSurveyForm(data=form_data)
        self.assertTrue(form.is_valid())
