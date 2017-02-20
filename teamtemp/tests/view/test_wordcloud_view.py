from django.core.urlresolvers import reverse
from django.test import TestCase


class WordcloudViewTestCases(TestCase):
    def test_wordcloud_view(self):
        response = self.client.get(reverse('wordcloud', kwargs={'word_list': ''}), follow=True)
        self.assertRedirects(response, '/media/blank.png')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'image/png')
        self.assertEqual(response['Cache-Control'], 'public, max-age=315360000')
        self.assertGreater(len(response.getvalue()), 0)
