from django.test import TestCase
from django.test import Client

# Create your tests here.

class ViewTests(TestCase):
	def testAppView(self):
		resp = self.client.get('/app/')
		self.assertEqual(resp.status_code, 200)

	def testTestView(self):
		resp = self.client.get('/app/test/')
		self.assertEqual(resp.status_code, 200)

	def testProfile(self):
		resp = self.client.post('/app/profile/', {'user': 'DrkSephy'} )
		self.assertEqual(resp.status_code, 200)

	def testProfileContent(self):
		resp = self.client.post('/app/profile/', {'user': 'DrkSephy'} )
		self.assertNotEqual(resp.content, '')