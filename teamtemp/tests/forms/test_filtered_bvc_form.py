from django.test import TestCase

from teamtemp.tests.factories import TeamTemperatureFactory, TemperatureResponseFactory, TeamFactory, \
    TeamResponseHistoryFactory

from teamtemp.responses.models import TeamTemperature

from teamtemp.responses.forms import FilteredBvcForm

class FilteredBvcFormTestCases(TestCase):
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

        self.form_data = {
            'id': self.teamtemp.id,
            'filter_dept_names': ['d1', 'd2', 'd3'],
            'filter_site_names': ['s1', 's2', 's3'],
            'filter_region_names': ['r1', 'r2', 'r3'],
        }

    def test_empty_filtered_bvc_form(self):
        form = FilteredBvcForm(
            dept_names_list=['d1', 'd2', 'd3'],
            site_names_list=['s1', 's2', 's3'],
            region_names_list=['r1', 'r2', 'r3'],
        )
        self.assertFalse(form.is_valid())

    def test_existing_filtered_bvc_form(self):
        form = FilteredBvcForm(
            data=self.form_data,
            dept_names_list=['d1', 'd2', 'd3'],
            site_names_list=['s1', 's2', 's3'],
            region_names_list=['r1', 'r2', 'r3'],
            dept_names_list_on=['d1', 'd2', 'd3'],
            site_names_list_on=['s1', 's2', 's3'],
            region_names_list_on=['r1', 'r2', 'r3'],
        )
        self.assertTrue(form.is_valid())

    def test_bad_dept_name_filtered_bvc_form(self):
        self.form_data['filter_dept_names'] = ['d1', 'bad1'];
        form = FilteredBvcForm(
            data=self.form_data,
            dept_names_list=['d1', 'd2', 'd3'],
            site_names_list=['s1', 's2', 's3'],
            region_names_list=['r1', 'r2', 'r3'],
        )
        self.assertFalse(form.is_valid())
