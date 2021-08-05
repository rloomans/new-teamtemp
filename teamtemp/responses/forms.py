import re

import pytz
from builtins import object
from builtins import str
from django import forms
from django.forms.utils import ErrorList
from django.utils import timezone
from django.utils.html import escape
from django.utils.safestring import mark_safe

from teamtemp.responses.models import TeamTemperature, Teams, TemperatureResponse


def _clean_value(field_value, regex):
    matches = re.findall(regex, field_value)
    if matches:
        error = '"{names}" contains invalid characters ' '{matches}'.format(
            names=escape(field_value), matches=list({str(x) for x in matches}))
        raise forms.ValidationError(error)
    return field_value


def _clean_field(obj, field_name, regex):
    field_value = obj.cleaned_data[field_name]
    return _clean_value(field_value, regex)


def _clean_names_field_list(obj, field_name):
    names = obj.cleaned_data[field_name]
    for name in names:
        _clean_value(name, r'[^A-Za-z0-9_-]')
    return names


def _clean_names_field(obj, field_name):
    return _clean_field(obj, field_name, r'[^A-Za-z0-9,_-]')


def _clean_name_field(obj, field_name):
    return _clean_field(obj, field_name, r'[^A-Za-z0-9_-]')


def _clean_team_name_field(obj, field_name):
    team_name = re.sub(r' +', '_', obj.cleaned_data[field_name].strip())
    return _clean_value(team_name, r'[^\w-]')


def _check_passwords(obj, cleaned_data):
    new_password = cleaned_data.get('new_password')
    confirm_password = cleaned_data.get('confirm_password')

    if new_password:
        if not confirm_password:
            obj.add_error('confirm_password', 'Confirm the new password')
        elif new_password != confirm_password:
            obj.add_error(
                'new_password',
                'New password and confirmation must match')
            obj.add_error('confirm_password',
                          'New password and confirmation must match')


class ErrorBox(ErrorList):
    def __str__(self):
        return mark_safe(self.as_box())

    def as_box(self):
        if not self:
            return u''
        return u'<br/><div class="error box">%s</div>' % self.as_lines()

    def as_lines(self):
        return "<br/>".join(e for e in self)


class CreateSurveyForm(forms.Form):
    error_css_class = 'error box'

    new_password = forms.CharField(
        widget=forms.PasswordInput({'placeholder': '', 'autocomplete': 'new-password'}),
        max_length=256,
        label='Survey Password (so that you can see the admin pages if you change browser)')
    confirm_password = forms.CharField(
        widget=forms.PasswordInput({'placeholder': '', 'autocomplete': 'new-password-confirm'}),
        max_length=256, label='Confirm Survey Password')
    dept_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'DEPT1,DEPT2..',
                'size': '64'}),
        max_length=64,
        required=False,
        label='Department Names')
    region_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'REGION1,REGION2..',
                'size': '64'}),
        max_length=64,
        required=False,
        label='Region Names')
    site_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'SITE1,SITE2..',
                'size': '64'}),
        max_length=64,
        required=False,
        label='Site Names')

    def clean_dept_names(self):
        return _clean_names_field(self, 'dept_names')

    def clean_region_names(self):
        return _clean_names_field(self, 'region_names')

    def clean_site_names(self):
        return _clean_names_field(self, 'site_names')

    def clean(self):
        cleaned_data = super(CreateSurveyForm, self).clean()

        _check_passwords(self, cleaned_data)


class FilteredBvcForm(forms.Form):
    error_css_class = 'error box'

    def __init__(self, *args, **kwargs):
        dept_names_list = kwargs.pop('dept_names_list')
        region_names_list = kwargs.pop('region_names_list')
        site_names_list = kwargs.pop('site_names_list')

        dept_names_list_on = kwargs.pop(
            'dept_names_list_on') if 'dept_names_list_on' in kwargs else None
        region_names_list_on = kwargs.pop(
            'region_names_list_on') if 'region_names_list_on' in kwargs else None
        site_names_list_on = kwargs.pop(
            'site_names_list_on') if 'site_names_list_on' in kwargs else None

        super(FilteredBvcForm, self).__init__(*args, **kwargs)

        self.fields['filter_dept_names'] = forms.MultipleChoiceField(
            choices=[
                (x,
                 x) for x in dept_names_list],
            widget=forms.CheckboxSelectMultiple,
            required=False,
            initial=dept_names_list_on)
        self.fields['filter_region_names'] = forms.MultipleChoiceField(
            choices=[
                (x,
                 x) for x in region_names_list],
            widget=forms.CheckboxSelectMultiple,
            required=False,
            initial=region_names_list_on)
        self.fields['filter_site_names'] = forms.MultipleChoiceField(
            choices=[
                (x,
                 x) for x in site_names_list],
            widget=forms.CheckboxSelectMultiple,
            required=False,
            initial=site_names_list_on)

    def clean_filter_dept_names(self):
        return _clean_names_field_list(self, 'filter_dept_names')

    def clean_filter_site_names(self):
        return _clean_names_field_list(self, 'filter_site_names')

    def clean_filter_region_names(self):
        return _clean_names_field_list(self, 'filter_region_names')


class AddTeamForm(forms.ModelForm):
    class Meta(object):
        model = Teams
        fields = ['team_name', 'dept_name', 'region_name', 'site_name']

    error_css_class = 'error box'
    team_name = forms.CharField(max_length=64)
    dept_name = forms.CharField(max_length=64)
    site_name = forms.CharField(max_length=64)
    region_name = forms.CharField(max_length=64)

    def __init__(self, *args, **kwargs):
        dept_name_choices = []
        if 'dept_names_list' in kwargs:
            dept_name_choices = [(x, x) for x in kwargs.pop('dept_names_list')]
            dept_name_choices.append(('', '-'))

        region_name_choices = []
        if 'region_names_list' in kwargs:
            region_name_choices = [(x, x)
                                   for x in kwargs.pop('region_names_list')]
            region_name_choices.append(('', '-'))

        site_name_choices = []
        if 'site_names_list' in kwargs:
            site_name_choices = [(x, x) for x in kwargs.pop('site_names_list')]
            site_name_choices.append(('', '-'))

        super(AddTeamForm, self).__init__(*args, **kwargs)

        self.fields['dept_name'] = forms.ChoiceField(
            choices=dept_name_choices, initial='', required=False)
        self.fields['region_name'] = forms.ChoiceField(
            choices=region_name_choices, initial='', required=False)
        self.fields['site_name'] = forms.ChoiceField(
            choices=site_name_choices, initial='', required=False)

    def clean_team_name(self):
        return _clean_team_name_field(self, 'team_name')

    def clean_dept_name(self):
        return _clean_name_field(self, 'dept_name')

    def clean_site_name(self):
        return _clean_name_field(self, 'site_name')

    def clean_region_name(self):
        return _clean_name_field(self, 'region_name')


class SurveyResponseForm(forms.ModelForm):
    class Meta(object):
        model = TemperatureResponse
        fields = ['score', 'word']

    error_css_class = 'error box'
    score = forms.IntegerField(min_value=1, max_value=10)

    def __init__(self, *args, **kwargs):
        self.max_word_count = kwargs.pop('max_word_count')
        super(SurveyResponseForm, self).__init__(*args, **kwargs)

    def clean_score(self):
        score = self.cleaned_data['score']
        if int(score) < 1:
            raise forms.ValidationError('Temperature %s is too low' % score)
        if int(score) > 10:
            raise forms.ValidationError('Temperature %s is too high' % score)
        return score

    def clean_word(self):
        word = self.cleaned_data['word']
        _clean_value(word, r'[^A-Za-z0-9-]')

        word_count = len(word.split())
        if word_count > self.max_word_count:
            error = 'Max {max_word_count} Words'.format(
                max_word_count=escape(self.max_word_count))
            raise forms.ValidationError(error)

        return word.lower()


class ResultsPasswordForm(forms.Form):
    error_css_class = 'error box'
    password = forms.CharField(widget=forms.PasswordInput(), max_length=256)


class SurveySettingsForm(forms.ModelForm):
    error_css_class = 'error box'
    new_password = forms.CharField(widget=forms.PasswordInput(
        {'autocomplete': 'new-password'}), max_length=256, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        {'autocomplete': 'new-password-confirm'}), max_length=256, required=False)
    new_team_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'size': '64'}),
        max_length=64,
        required=False)
    current_team_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'size': '64'}),
        max_length=64,
        required=False)
    censored_word = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'size': '64'}),
        max_length=64,
        required=False)
    dept_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'size': '64'}),
        max_length=64,
        required=False)
    region_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'size': '64'}),
        max_length=64,
        required=False)
    site_names = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'size': '64'}),
        max_length=64,
        required=False)
    default_tz = forms.ChoiceField(
        choices=[(x, x) for x in pytz.all_timezones], required=False)
    next_archive_date = forms.DateField(widget=forms.DateInput(
        attrs={
            'type': 'date',
            'class': 'datepicker',
            'pattern': '(?:19|20)[0-9]{2}-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1[0-9]|2[0-9])|(?:(?!02)(?:0[1-9]|1[0-2])-(?:30))|(?:(?:0[13578]|1[02])-31))'
        },
        format='%Y-%m-%d'), required=False)
    max_word_count = forms.IntegerField(min_value=1, max_value=5)

    class Meta(object):
        model = TeamTemperature
        fields = [
            'archive_schedule',
            'survey_type',
            'dept_names',
            'region_names',
            'site_names',
            'default_tz',
            'max_word_count',
            'next_archive_date']

    def clean_archive_schedule(self):
        archive_schedule = self.cleaned_data['archive_schedule']
        if int(archive_schedule) > 28:
            raise forms.ValidationError('Archive Schedule Max 28 Days')
        return archive_schedule

    def clean_next_archive_date(self):
        next_archive_date = self.cleaned_data['next_archive_date']
        if next_archive_date is not None and next_archive_date < timezone.now().date():
            raise forms.ValidationError('Next Archive Date must not be past')
        return next_archive_date

    def clean_survey_type(self):
        survey_type = self.cleaned_data['survey_type']
        if survey_type not in [
            'TEAMTEMP',
            'CUSTOMERFEEDBACK',
                'DEPT-REGION-SITE']:
            raise forms.ValidationError(
                'Supported Survey Types: TEAMTEMP and CUSTOMERFEEDBACK only')
        return survey_type

    def clean_dept_names(self):
        return _clean_names_field(self, 'dept_names')

    def clean_region_names(self):
        return _clean_names_field(self, 'region_names')

    def clean_site_names(self):
        return _clean_names_field(self, 'site_names')

    def clean_default_tz(self):
        return _clean_field(self, 'default_tz', r'[^A-Za-z0-9-/]')

    def clean_max_word_count(self):
        max_word_count = self.cleaned_data['max_word_count']
        if 1 > int(max_word_count) > 5:
            raise forms.ValidationError(
                'Max Word Count Min Value = 1, Max Value = 5')
        return max_word_count

    def clean_new_team_name(self):
        return _clean_team_name_field(self, 'new_team_name')

    def clean(self):
        cleaned_data = super(SurveySettingsForm, self).clean()

        _check_passwords(self, cleaned_data)
