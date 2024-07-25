from django.test import TestCase, Client
from salesdata.models import SalesData
from salesdata.serializers import SalesDataSerializer
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
        jdata =  json.loads(data.content)
        self.assertEqual(jdata, response_model)
       
    
    def test_w_1_more_product(self):
        from .filltable import fill
        fill()
        fill_data = SalesData.objects.all()
        self.assertEqual(len(fill_data),800)
        client = Client()

        data = self.client.get('/nus')
        jdata =  json.loads(data.content)

        prod_data = {
        "sale_date": "2024-04-16",
        "product_id": "100",
        "product_title": "adaptador usb-c para p2",
        "product_image_url": "https://www.lorempixel.com/67/706",
        "store_name": "Submarino",
        "store_id": "20",
        "sales_per_day": "1000",
        "product_price": "10.00"}
        s = SalesData.objects.create(**prod_data)
        #print("s:", s)

        client = Client()
        new_product = SalesDataSerializer(SalesData.objects.get(id = s.id)).data
       
        #print("w_new:\n", jdata[1:]+[new_product],len(jdata[1:]+[new_product]))
        data = self.client.get('/nus')
        jdata_new =  json.loads(data.content)
        #print("jnew:\n", jdata_new, len(jdata_new))
        self.assertEqual(jdata_new,  jdata[1:]+[new_product])
       

        
