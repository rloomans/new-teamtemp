from builtins import object
import hashlib
import random
import string

import factory
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from factory.fuzzy import FuzzyInteger, FuzzyDecimal, FuzzyText
from factory_djoy import CleanModelFactory
from faker import Faker

from teamtemp import utils
from teamtemp.responses.models import TeamResponseHistory, Teams, \
    TeamTemperature, TemperatureResponse, User, WordCloudImage
from teamtemp.views import DEFAULT_WORDCLOUD_HEIGHT, DEFAULT_WORDCLOUD_WIDTH

fake = Faker()


class UserFactory(CleanModelFactory):
    class Meta(object):
        model = User
        django_get_or_create = ('id',)

    id = FuzzyText(length=32, chars=utils.chars)


class TeamTemperatureFactory(CleanModelFactory):
    class Meta(object):
        model = TeamTemperature
        django_get_or_create = ('id',)

    id = FuzzyText(length=8, chars=utils.chars)
    creator = factory.SubFactory(UserFactory)
    password = make_password('testing')


class TeamFactory(CleanModelFactory):
    class Meta(object):
        model = Teams
        django_get_or_create = ('team_name',)

    request = factory.SubFactory(TeamTemperatureFactory)
    team_name = FuzzyText(
        length=random.randint(
            1, 64), chars=(
            utils.chars + '_-'))


class TemperatureResponseFactory(CleanModelFactory):
    class Meta(object):
        model = TemperatureResponse

    request = factory.SubFactory(TeamTemperatureFactory)
    responder = factory.SubFactory(UserFactory)
    score = FuzzyInteger(1, 10)
    word = FuzzyText(
        length=random.randint(
            2, 32), chars=(
            string.ascii_letters + '-'))
    response_date = factory.LazyFunction(timezone.now)
    team_name = FuzzyText(
        length=random.randint(
            1, 64), chars=(
            utils.chars + '_-'))


class TeamResponseHistoryFactory(CleanModelFactory):
    class Meta(object):
        model = TeamResponseHistory

    request = factory.SubFactory(TeamTemperatureFactory)
    average_score = FuzzyDecimal(1, 10, 5)
    responder_count = FuzzyInteger(1, 25)
    team_name = FuzzyText(
        length=random.randint(
            1, 64), chars=(
            utils.chars + '_-'))
    archive_date = factory.LazyFunction(timezone.now)

    @factory.lazy_attribute
    def word_list(self):
        return fake.words(nb=self.responder_count)


class WordCloudImageFactory(CleanModelFactory):
    class Meta(object):
        model = WordCloudImage

    word_list = ' '.join(fake.words(nb=random.randint(1, 25)))
    width = DEFAULT_WORDCLOUD_WIDTH
    height = DEFAULT_WORDCLOUD_HEIGHT
    image_url = "/%s/%s" % (fake.uri_path(), fake.file_name(category='image'))
    creation_date = factory.LazyFunction(timezone.now)

    @factory.lazy_attribute
    def word_hash(self):
        return hashlib.sha1(self.word_list.encode('utf-8')).hexdigest()
