from django.test import TestCase

from teamtemp.responses.forms import SurveyResponseForm
from teamtemp.tests.factories import TeamTemperatureFactory, TemperatureResponseFactory


class SurveyResponseFormTestCases(TestCase):
    def setUp(self):
        self.survey = TeamTemperatureFactory()
        self.response = TemperatureResponseFactory(request=self.survey)
        self.form_data = {
            'response_id': self.response.id,
            'survey_type_title': 'test',
            'temp_question_title': 'test',
            'word_question_title': 'test',
            'team_name': self.response.team_name,
            'pretty_team_name': self.response.pretty_team_name(),
            'id': self.survey.id,
            'word': self.response.word,
            'score': self.response.score,
        }

    def test_empty_survey_response_form(self):
        form = SurveyResponseForm(max_word_count=1)
        self.assertFalse(form.is_valid())

    def test_existing_survey_response_form(self):
        form = SurveyResponseForm(data=self.form_data, max_word_count=1)
        self.assertTrue(form.is_valid())

    def test_invalid_word_survey_response_form(self):
        self.form_data['word'] = 'bad!test'
        form = SurveyResponseForm(data=self.form_data, max_word_count=1)
        self.assertFalse(form.is_valid())

    def test_invalid_score_survey_response_form(self):
        self.form_data['score'] = 11
        form = SurveyResponseForm(data=self.form_data, max_word_count=1)
        self.assertFalse(form.is_valid())

    def test_multiple_words_survey_response_form(self):
        self.form_data['word'] = 'test one two three'
        form = SurveyResponseForm(data=self.form_data, max_word_count=4)
        self.assertTrue(form.is_valid())

    def test_too_many_words_survey_response_form(self):
        self.form_data['word'] = 'test one two three'
        form = SurveyResponseForm(data=self.form_data, max_word_count=2)
        self.assertFalse(form.is_valid())
