from builtins import object
from rest_framework import serializers

from .models import TeamResponseHistory, TeamTemperature, Teams, TemperatureResponse, User, WordCloudImage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = User
        fields = (
            'url',
            'id',
            'creation_date',
            'team_temperatures',
            'temperature_responses')


class WordCloudImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = WordCloudImage
        fields = (
            'url',
            'id',
            'creation_date',
            'word_list',
            'width',
            'height',
            'word_hash',
            'image_url')


class TeamTemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = TeamTemperature
        fields = ('url', 'id', 'creation_date', 'creator', 'archive_schedule',
                  'archive_date', 'survey_type', 'default_tz',
                  'max_word_count', 'dept_names', 'site_names',
                  'region_names', 'creation_date', 'modified_date', 'teams',
                  'team_response_histories', 'temperature_responses')


class TemperatureResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = TemperatureResponse
        fields = (
            'url',
            'id',
            'request',
            'responder',
            'score',
            'word',
            'team_name',
            'archived',
            'response_date',
            'archive_date')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = Teams
        fields = (
            'url',
            'id',
            'request',
            'team_name',
            'dept_name',
            'site_name',
            'region_name',
            'creation_date',
            'modified_date')


class TeamResponseHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta(object):
        model = TeamResponseHistory
        fields = (
            'url',
            'id',
            'request',
            'average_score',
            'word_list',
            'responder_count',
            'team_name',
            'archive_date')
