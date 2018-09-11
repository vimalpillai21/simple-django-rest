from django.shortcuts import render
from .serializers import HelloSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet 
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
    
class HelloViewSet(ViewSet):
    "This is a simple view set"
    serializer_class = HelloSerializer
    def list(self,request):
        "Returns a hello message"
        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code.'
        ]
        return Response({'message':'Hello!','a_viewset':a_viewset})
    
    def create(self,request):
        "Create a new hello message"
        serializer = HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        "Handles getting object by its id"
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        "Handles updating object by its id"
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        "Handles Partial_updating object by its id"
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        "Handles deletion object by its id"
        return Response({'http_method':'DELETE'})
    