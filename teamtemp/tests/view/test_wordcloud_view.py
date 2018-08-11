from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from teamtemp.tests.factories import WordCloudImageFactory


class WordcloudViewTestCases(TestCase):
    def assertWordCloudImage(
            self,
            response,
            expected_url='/media/blank.png',
            status_code=status.HTTP_302_FOUND):
        self.assertRedirects(
            response,
            expected_url=expected_url,
            status_code=status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'image/png')
        self.assertEqual(
            response['Cache-Control'],
            'public, max-age=315360000')
        self.assertGreater(len(response.getvalue()), 0)

    def test_wordcloud_view_blank(self):
        response = self.client.get(
            reverse(
                'wordcloud',
                kwargs={
                    'word_hash': ''}),
            follow=True)
        self.assertWordCloudImage(response, '/media/blank.png')

    def test_wordcloud_view_missing(self):
        response = self.client.get(
            reverse(
                'wordcloud',
                kwargs={
                    'word_hash': '0123456789abcdef0123456789abcdef01234567'}),
            follow=True)
        self.assertWordCloudImage(response, '/media/blank.png')

    def test_wordcloud_view_found(self):
        word_cloud_image = WordCloudImageFactory(image_url='/media/test.png')
        response = self.client.get(
            reverse(
                'wordcloud',
                kwargs={
                    'word_hash': word_cloud_image.word_hash}),
            follow=True)
        self.assertWordCloudImage(
            response,
            word_cloud_image.image_url,
            status.HTTP_302_FOUND)
