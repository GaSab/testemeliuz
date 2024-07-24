from django.shortcuts import render
from models import SalesData
from queries.retrive_most_sold import retrieve_query

# Create your views here.
def new_user(request):
    if request.method == 'GET':
        SalesData.object.raw(retrieve_query)
        return None