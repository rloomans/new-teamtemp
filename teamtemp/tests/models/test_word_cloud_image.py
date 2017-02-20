from builtins import str
from django.test import TestCase

from teamtemp.tests.factories import WordCloudImageFactory


class WordCloudImageTestCases(TestCase):
    def test_wordcloud(self):
        wordcloud = WordCloudImageFactory()
        self.assertTrue(len(wordcloud.word_list) > 0)
        self.assertTrue(len(wordcloud.word_hash) > 0)
        self.assertTrue(len(wordcloud.image_url) > 0)
        self.assertIsNotNone(wordcloud.creation_date)
        self.assertIsNotNone(wordcloud.modified_date)
        self.assertEqual(str(wordcloud), "%s: %s %s %s %s" % (
            wordcloud.id, wordcloud.creation_date, wordcloud.word_hash, wordcloud.word_list, wordcloud.image_url))
