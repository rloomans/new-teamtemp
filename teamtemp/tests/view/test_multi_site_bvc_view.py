from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from teamtemp.tests.factories import TeamTemperatureFactory, TemperatureResponseFactory, TeamFactory, \
    TeamResponseHistoryFactory

from teamtemp.responses.models import TeamTemperature


class MultiSiteBvcViewTestCases(TestCase):
    def setUp(self):
        self.teamtemp = TeamTemperatureFactory(
            survey_type=TeamTemperature.DEPT_REGION_SITE,
            dept_names='d1 d2 d3',
            site_names='s1 s2 s3',
            region_names='r1 r2 r3'
        )
        self.team1 = TeamFactory(request=self.teamtemp, dept_name='d1', site_name='s1', region_name='r1')
        self.team2 = TeamFactory(request=self.teamtemp, dept_name='d2', site_name='s2', region_name='r2')
        self.team3 = TeamFactory(request=self.teamtemp, dept_name='d3', site_name='s3', region_name='r3')
        self.response = TemperatureResponseFactory(
            request=self.teamtemp, team_name=self.team1.team_name)

        self.team_history = TeamResponseHistoryFactory(
            request=self.teamtemp, team_name=self.team1.team_name)

        self.response = TemperatureResponseFactory(
            request=self.teamtemp, team_name=self.team1.team_name,
            archived=True, archive_date=self.team_history.archive_date)

        self.history = TeamResponseHistoryFactory(request=self.teamtemp, team_name='Average')

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
                    'team_name': self.team1.team_name}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bvc_historical_no_team_view(self):
        response = self.client.get(
            reverse(
                'bvc',
                kwargs={
                    'survey_id': self.teamtemp.id,
                    'archive_id': self.history.id}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bvc_historical_team_view(self):
        response = self.client.get(
            reverse(
                'bvc',
                kwargs={
                    'survey_id': self.teamtemp.id,
                    'team_name': self.team1.team_name,
                    'archive_id': self.team_history.id}))
        self.assertTemplateUsed(response, 'bvc.html')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
