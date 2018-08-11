from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from teamtemp.tests.factories import TeamTemperatureFactory, TemperatureResponseFactory, TeamFactory, \
    TeamResponseHistoryFactory


class BvcViewTestCases(TestCase):
    def setUp(self):
        self.teamtemp = TeamTemperatureFactory()
        self.team = TeamFactory(request=self.teamtemp)
        self.response = TemperatureResponseFactory(
            request=self.teamtemp, team_name=self.team.team_name)

        TeamResponseHistoryFactory(
            request=self.teamtemp,
            team_name=self.team.team_name)
        TeamResponseHistoryFactory(request=self.teamtemp, team_name='Average')

    def test_bvc_no_team_view(self):
        response = self.client.get(
            reverse(
                'bvc', kwargs={
                    'survey_id': self.teamtemp.id}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bvc_team_view(self):
        response = self.client.get(
            reverse(
                'bvc',
                kwargs={
                    'survey_id': self.teamtemp.id,
                    'team_name': self.team.team_name}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bvc_historical_no_team_view(self):
        history = TeamResponseHistoryFactory(
            request=self.teamtemp, team_name=self.team.team_name)
        response = self.client.get(
            reverse(
                'bvc',
                kwargs={
                    'survey_id': self.teamtemp.id,
                    'archive_id': history.id}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bvc_historical_team_view(self):
        history = TeamResponseHistoryFactory(
            request=self.teamtemp, team_name=self.team.team_name)
        response = self.client.get(
            reverse(
                'bvc',
                kwargs={
                    'survey_id': self.teamtemp.id,
                    'team_name': self.team.team_name,
                    'archive_id': history.id}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
