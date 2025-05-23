import sys

from django.urls import reverse
from django.test import TestCase
from rest_framework import status

from teamtemp.tests.factories import WordCloudImageFactory
from teamtemp.responses.models import WordCloudImage


class WordcloudViewTestCases(TestCase):
    def assertWordCloudImage(self, response, expected_url='/media/blank.png', status_code=status.HTTP_302_FOUND):
        self.assertRedirects(response, expected_url=expected_url, status_code=status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'image/png')
        self.assertEqual(response['Cache-Control'], 'public, max-age=315360000')
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

    def test_wordcloud_view_found_with_size(self):
        word_cloud_image = WordCloudImageFactory(image_url='/media/test.png', width=600, height=300)
        response = self.client.get(
            reverse(
                'wordcloud',
                kwargs={
                    'word_hash': word_cloud_image.word_hash,
                    'width': 600,
                    'height': 300
                }),
            follow=True)
        self.assertWordCloudImage(
            response,
            word_cloud_image.image_url,
            status.HTTP_302_FOUND)

    def test_wordcloud_view_request_with_invalid_width(self):
        word_cloud_image = WordCloudImageFactory(image_url='/media/test.png')
        response = self.client.get(
            reverse(
                'wordcloud',
                kwargs={
                    'word_hash': word_cloud_image.word_hash,
                    'width': 9999,
                    'height': 300
                }),
            follow=True)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wordcloud_view_request_with_invalid_height(self):
        word_cloud_image = WordCloudImageFactory(image_url='/media/test.png')
        response = self.client.get(
            reverse(
                'wordcloud',
                kwargs={
                    'word_hash': word_cloud_image.word_hash,
                    'width': 9999,
                    'height': 300
                }),
            follow=True)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wordcloud_view_generate(self):
        word_cloud_image = WordCloudImageFactory(image_url=None)
        response = self.client.get(
            reverse(
                'wordcloud',
                kwargs={
                    'word_hash': word_cloud_image.word_hash}),
            follow=True)

        word_cloud_image2 = WordCloudImage.objects.get(id=word_cloud_image.id)

        self.assertRedirects(response, expected_url=word_cloud_image2.image_url, status_code=status.HTTP_302_FOUND)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'image/png')
        self.assertEqual(response['Cache-Control'], 'public, max-age=315360000')
        self.assertGreater(len(response.getvalue()), 0)
