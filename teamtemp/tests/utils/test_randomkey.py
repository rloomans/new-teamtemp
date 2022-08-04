from django.test import TestCase, RequestFactory

from teamtemp.utils.randomkey import randomkey, RANDOM_KEY_LEN


class UtilsTestCases(TestCase):
    def test_randomkey(self):
        key = randomkey()
        self.assertIsNotNone(key)
        self.assertEqual(len(key), RANDOM_KEY_LEN)
