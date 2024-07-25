from rest_framework import serializers
from salesdata.models import SalesData

class SugestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesData
        fields = ('id','sale_date','product_id','product_title','product_image_url','store_name','store_id','sales_per_day','product_price')

class SalesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesData
        fields = ('id','sale_date','product_id','product_title','product_image_url','store_name','store_id','sales_per_day','product_price')