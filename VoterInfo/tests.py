# VoterInfo/tests.py
from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):

    def test_MyInfo_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_NextElection_page_status_code(self):
        response = self.client.get('/NextElection/')
        self.assertEqual(response.status_code, 200)
