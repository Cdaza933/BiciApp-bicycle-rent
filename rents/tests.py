import json
from time import sleep
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
from bicycles.models import Bicycle
from django.test import TestCase
from rest_framework.test import APIClient
from rents.models import Rent

class AddOpenQuestionTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/rent/'
        self.headers = {'Content-Type': 'application/json'}
        self.bicycle = Bicycle.objects.all().first()
        self.payload = {"bicycle_id": self.bicycle.pk, "user_id": "00urb1mlhrHkuYe4e0h7"}


    def test_rent_bicycle(self):
        response = self.client.post(self.url,  self.payload, format='json')
        current_data = response.content
        self.assertTrue(Rent.objects.filter(pk=current_data).exists())
        return current_data

    def test_cost_bicycles(self):
        rent_pk = self.test_rent_bicycle()
        response = self.client.put(self.url, {'id':rent_pk}, format='json')
        current_data = json.loads(response.content)
        self.assertEquals(current_data['total_value'], self.bicycle.price * current_data['total_minutes'])
