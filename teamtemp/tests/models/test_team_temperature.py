from builtins import str
import re
from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory, UserFactory


class TeamTemperatureTestCases(TestCase):
    def test_team_temperature(self):
        teamtemp = TeamTemperatureFactory()
        self.assertTrue(len(teamtemp.id) > 0)
        self.assertIsNotNone(teamtemp.creation_date)
        self.assertIsNotNone(teamtemp.modified_date)
        self.assertEqual(teamtemp.survey_type, 'TEAMTEMP')
        self.assertRegexpMatches(str(teamtemp), "%s: %s %s " % (
            teamtemp.id, teamtemp.creator.id, re.escape(str(teamtemp.creation_date))))

        stats, query_set = teamtemp.stats()
        self.assertEqual(stats['count'], 0)
        self.assertIsNone(stats['average']['score__avg'])
        self.assertEqual(stats['words'].count(), 0)
        self.assertEqual(query_set.count(), 0)

    def test_customer_feedback(self):
        teamtemp = TeamTemperatureFactory(survey_type='CUSTOMERFEEDBACK')
        self.assertTrue(len(teamtemp.id) > 0)
        self.assertIsNotNone(teamtemp.creation_date)
        self.assertIsNotNone(teamtemp.modified_date)
        self.assertEqual(teamtemp.survey_type, 'CUSTOMERFEEDBACK')

    def test_uniq_teamtemp_ids(self):
        self.assertNotEqual(
            TeamTemperatureFactory().id,
            TeamTemperatureFactory().id)

    def test_multiple_surveys_for_user(self):
        user = UserFactory()
        teamtemp1 = TeamTemperatureFactory(creator=user)
        teamtemp2 = TeamTemperatureFactory(creator=user)
        self.assertNotEqual(teamtemp1.id, teamtemp2.id)
        self.assertEqual(teamtemp1.creator.id, teamtemp2.creator.id)
        self.assertEqual(user.team_temperatures.count(), 2)

    def test_duplicate_teamtemp_ids(self):
        with self.assertRaises(RuntimeError):
            TeamTemperatureFactory(id='bob')
            TeamTemperatureFactory(id='bob')

    def test_invalid_max_word_count(self):
        with self.assertRaises(RuntimeError):
            TeamTemperatureFactory(max_word_count=0)
        with self.assertRaises(RuntimeError):
            TeamTemperatureFactory(max_word_count=11)
