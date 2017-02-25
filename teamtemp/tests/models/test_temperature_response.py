from __future__ import division
from builtins import str
from past.utils import old_div
import itertools

from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory, TemperatureResponseFactory, UserFactory


class TemperatureResponseTestCases(TestCase):
    def test_response(self):
        response = TemperatureResponseFactory()
        self.assertTrue(len(response.word) > 0)
        self.assertTrue(response.score > 0)
        self.assertTrue(len(response.team_name) > 0)
        self.assertIsNotNone(response.response_date)
        self.assertIsNotNone(response.request)
        self.assertRegexpMatches(str(response), "^%d: %s %s %d %s %s " % (
            response.id, response.request.id, response.responder.id, response.score, response.word, response.team_name))

        stats, query_set = response.request.stats()
        self.assertEqual(stats['count'], 1)
        self.assertEqual(stats['average']['score__avg'], float(response.score))
        self.assertEqual(stats['words'][0]['word'], response.word)

        self.assertEqual(query_set.count(), 1)

    def test_multiple_responses_for_user_and_survey(self):
        user = UserFactory()
        teamtemp1 = TeamTemperatureFactory()
        teamtemp2 = TeamTemperatureFactory()
        _ = TemperatureResponseFactory(request=teamtemp1, responder=user)
        _ = TemperatureResponseFactory(request=teamtemp2, responder=user)
        self.assertEqual(user.temperature_responses.count(), 2)
        self.assertEqual(teamtemp1.temperature_responses.count(), 1)
        self.assertEqual(teamtemp2.temperature_responses.count(), 1)

    def test_multiple_responses_for_a_survey(self):
        teamtemp = TeamTemperatureFactory()
        response1 = TemperatureResponseFactory(request=teamtemp)
        response2 = TemperatureResponseFactory(request=teamtemp)
        response3 = TemperatureResponseFactory(request=teamtemp, word=response2.word)
        self.assertEqual(teamtemp.temperature_responses.count(), 3)

        stats, query_set = teamtemp.stats()

        self.assertEqual(stats['count'], 3)
        self.assertEqual(stats['average']['score__avg'],
                         old_div(float(response1.score + response2.score + response3.score), 3))

        words = [[x['word']] * x['id__count'] for x in stats['words']]
        flat_words = sorted(itertools.chain(*words))

        self.assertEqual(flat_words, sorted([response1.word, response2.word, response3.word]))

        self.assertEqual(query_set.count(), 3)
