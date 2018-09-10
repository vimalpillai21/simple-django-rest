from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    "Test API View"
    def get(self,request,format=None):
        "Returns a list of API View"
        
        an_apiview = [
        'Uses HTTPS method as function (get,patch,put,delete)',
        'It is similar to traditional django view',
        'Gives youn the most control over your logic',
        'Its manually mapped to URLs'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview}) 
