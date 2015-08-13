from django.test import TestCase
from django.test import Client

# Create your tests here.

class SimpleViewTest(TestCase):
	def testAppView(self):
		resp = self.client.get('/app/')
		self.assertEqual(resp.status_code, 200)
