from django.db import models

# Create your models here.
class SalesData(models.Model):
    sale_date = models.CharField(
        max_length=20
    )
    product_id = models.IntegerField()
    product_title = models.CharField(
       max_length=100
    )
    product_price = models.FloatField()
    product_image_url = models.CharField(
        max_length=100
    )
    store_name = models.CharField(
       max_length=50
    )
    store_id = models.IntegerField()
    sales_per_day = models.IntegerField()  