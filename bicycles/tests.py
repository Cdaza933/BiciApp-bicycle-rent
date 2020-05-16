from django.test import TestCase

# Create your tests here.
import json
import os
from random import randint
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
from bicycles.models import Bicycle
from django.test import TestCase
from rest_framework.test import APIClient


class AddOpenQuestionTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/bicycle/'
        self.headers = {'Content-Type': 'application/json'}
        self.nit = "3"
        if Bicycle.objects.filter(company_id=self.nit).exists():
            self.nit += str(randint(0, 10))
        self.payload = [
            {
            "company_id": self.nit,
            "company_name": self.nit,
            "price": 33.13,
            "model": "1",
            "address": "pass",
            },
            {
                "company_id": self.nit,
                "company_name": self.nit,
                "price": 32.13,
                "model": "2",
                "address": "pass",
            },
            {
                "company_id": self.nit,
                "company_name": self.nit,
                "price": 31.13,
                "model": "3",
                "address": "pass",
            }
        ]

    def test_add_bicycle(self):
        for payload in self.payload:
           self.client.post(self.url,  payload, format='json')
        bicycles = Bicycle.objects.filter(company_id=self.nit)
        self.assertTrue(bicycles.exists())

    def test_get_bicycles(self):
        self.test_add_bicycle()
        Bicycle.objects.all().exclude(company_id=self.nit).delete()
        bicycles = Bicycle.objects.filter(company_id=self.nit)
        response = self.client.get(self.url)
        current_data = json.loads(response.content)
        for bicycle_dict in current_data:
            bicycle = bicycles.filter(model=bicycle_dict['model']).first()
            self.assertNotEquals(bicycle, None)
            self.assertEqual(bicycle.price, bicycle_dict['price'])
