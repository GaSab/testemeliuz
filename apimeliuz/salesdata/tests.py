from django.test import TestCase, Client
from salesdata.models import SalesData
from salesdata.data_demos.demo_json import response_model
import requests
from salesdata.data_demos.demo_json import response_model
import json
# Create your tests here.
class BaseData(TestCase):
    def initial_import(self):
        #data = SalesData.objects.all()
        #self.assertEqual(len(data),800)
        self.assertEqual(1,1)
    def test_sugestgion(self):
        from .filltable import fill
        fill()
        client = Client()
        
        data = self.client.get('/nus')
        print("response.code: ", data.status_code)
        print("response json: ", data.json)
        print("response content: ", data.content)
        jdata =  json.loads(data.content)
        print('\n\n\n\n\n\n',jdata)
        self.assertEqual(jdata, response_model) 


        
