from builtins import str
from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory, TeamFactory


class TeamTestCases(TestCase):
    def test_team(self):
        team = TeamFactory()
        self.assertTrue(len(team.team_name) > 0)
        self.assertIsNotNone(team.creation_date)
        self.assertIsNotNone(team.modified_date)
        self.assertRegexpMatches(
            str(team), "^%d: %s %s " %
            (team.id, team.request.id, team.team_name))

    def test_pretty_team_name(self):
        team = TeamFactory(team_name='bob_and_his_friends')
        self.assertEqual(team.pretty_team_name(), 'bob and his friends')

    def test_uniq_team_names(self):
        self.assertNotEqual(TeamFactory().team_name, TeamFactory().team_name)

    def test_multiple_surveys_for_user(self):
        teamtemp = TeamTemperatureFactory()
        team1 = TeamFactory(request=teamtemp)
        team2 = TeamFactory(request=teamtemp)
        self.assertNotEqual(team1.team_name, team2.team_name)
        self.assertEqual(team1.request.id, team2.request.id)
        self.assertEqual(teamtemp.teams.count(), 2)

    def test_duplicate_team_names(self):
        teamtemp = TeamTemperatureFactory()
        with self.assertRaises(RuntimeError):
            TeamFactory(team_name='bob', request=teamtemp)
            TeamFactory(team_name='bob', request=teamtemp)

    def test_duplicate_team_names_for_different_requests(self):
        team1 = TeamFactory(team_name='bob')
        team2 = TeamFactory(team_name='bob')
        self.assertNotEqual(team1.request.id, team2.request.id)
        self.assertEqual(team1.team_name, team2.team_name)
