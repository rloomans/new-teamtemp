from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory
from teamtemp.responses.forms import CreateSurveyForm


class CreateSurveyFormTestCases(TestCase):
    def setUp(self):
        self.survey = TeamTemperatureFactory()
        self.form_data = {
            'id': self.survey.id,
            'new_password': self.survey.password,
            'confirm_password': self.survey.password,
            'dept_names': self.survey.dept_names,
            'region_names': self.survey.region_names,
            'site_names': self.survey.site_names,
        }

    def test_empty_survey_settings_form(self):
        form = CreateSurveyForm()
        self.assertFalse(form.is_valid())

    def test_existing_survey_settings_form(self):
        form = CreateSurveyForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_missing_confirm_password_survey_settings_form(self):
        self.form_data["confirm_password"] = ""
        form = CreateSurveyForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_password_mismatch_survey_settings_form(self):
        self.form_data["confirm_password"] = "two"
        form = CreateSurveyForm(data=self.form_data)
        self.assertFalse(form.is_valid())
