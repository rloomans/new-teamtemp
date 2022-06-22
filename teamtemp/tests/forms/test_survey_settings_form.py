from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory
from teamtemp.responses.forms import SurveySettingsForm


class SurveySettingsFormTestCases(TestCase):
    def test_empty_survey_settings_form(self):
        form = SurveySettingsForm()
        self.assertFalse(form.is_valid())

    def test_existing_survey_settings_form(self):
        survey = TeamTemperatureFactory()
        form_data = {
            'id': survey.id,
            'creator': survey.creator,
            'password': survey.password,
            'archive_schedule': survey.archive_schedule,
            'survey_type': survey.survey_type,
            'default_tz': survey.default_tz,
            'max_word_count': survey.max_word_count
        }
        form = SurveySettingsForm(data=form_data)
        self.assertTrue(form.is_valid())
