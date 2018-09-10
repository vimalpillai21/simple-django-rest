from django.shortcuts import render
from .serializers import HelloSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST
# Create your views here.

class HelloApiView(APIView):
    "Test API View"
    serializer_class = HelloSerializer
    
    
    def get(self,request,format=None):
        "Returns a list of API View"
        
        an_apiview = [
        'Uses HTTPS method as function (get,patch,put,delete)',
        'It is similar to traditional django view',
        'Gives youn the most control over your logic',
        'Its manually mapped to URLs'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview}) 
    
    def post(self,request):
        "Request Message"
                
        serializer = HelloSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            name = serializer.data.get('name')
            print(name)
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )
            
    def put(self,request,pk=None):
        "method is put"
        return Response({'method':'put'})
    
    def patch(self,request,pk=None):
        "method is patch"
        return Response({'method':'patch'})
    
    def delete(self,request,pk=None):
        "method is delete"
        return Response({'method':'delete'})