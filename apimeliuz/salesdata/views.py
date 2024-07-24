from django.shortcuts import render
from salesdata.models import SalesData
from salesdata.queries.retrive_most_sold import retrieve_query
from django.views.decorators.csrf import csrf_exempt
#from rest_framework.parsers import JSONParser
from salesdata.serializers import SugestionSerializer
from django.http.response import JsonResponse




# Create your views here.
@csrf_exempt
def new_user_sugestion(request):
    if request.method == 'GET':
        sugestions = SalesData.objects.raw(retrieve_query)
        sugestions_ser = SugestionSerializer(sugestions, many=True)
        return JsonResponse(sugestions_ser.data, safe=False)
    elif request.method == 'POST':
        return None
    elif request.method == 'PUT':
        return None
    elif request.method == 'DELETE':
        return None