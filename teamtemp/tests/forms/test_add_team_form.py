from django.test import TestCase

from teamtemp.responses.forms import AddTeamForm
from teamtemp.tests.factories import TeamTemperatureFactory


class AddTeamFormTestCases(TestCase):
    def test_empty_add_team_form(self):
        survey = TeamTemperatureFactory()
        form = AddTeamForm(data={'request': survey})
        self.assertFalse(form.is_valid())

    def test_existing_survey_settings_form(self):
        survey = TeamTemperatureFactory()
        form_data = {
            'request': survey,
            'team_name': 'test',
        }
        form = AddTeamForm(data=form_data)
        self.assertTrue(form.is_valid())
