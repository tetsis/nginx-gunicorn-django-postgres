from django.test import TestCase
from django.test.client import Client
from model.models import Table

# Create your tests here.

class PageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_top_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_save(self):
        response = self.client.get('/save/')
        self.assertEqual(response.status_code, 302)
        save_data = Table.objects.all()
        self.assertEqual(len(save_data), 1)