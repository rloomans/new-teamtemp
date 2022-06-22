from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory
from teamtemp.responses.forms import SurveySettingsForm


class SurveySettingsFormTestCases(TestCase):
    def setUp(self):
        self.survey = TeamTemperatureFactory()
        self.form_data = {
            'id': self.survey.id,
            'creator': self.survey.creator,
            'password': self.survey.password,
            'archive_schedule': self.survey.archive_schedule,
            'survey_type': self.survey.survey_type,
            'default_tz': self.survey.default_tz,
            'max_word_count': self.survey.max_word_count,
            'dept_names': self.survey.dept_names,
            'region_names': self.survey.region_names,
            'site_names': self.survey.site_names,
        }

    def test_empty_survey_settings_form(self):
        form = SurveySettingsForm()
        self.assertFalse(form.is_valid())

    def test_existing_survey_settings_form(self):
        form = SurveySettingsForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_tz_survey_settings_form(self):
        self.form_data["default_tz"] = "toast"
        form = SurveySettingsForm(data=self.form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_archive_schedule_survey_settings_form(self):
        self.form_data["archive_schedule"] = 99
        form = SurveySettingsForm(data=self.form_data)
        self.assertFalse(form.is_valid())
