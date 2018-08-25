from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import serializers

# Create your views here.


class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """ Returns a list of APIView features. """

        an_apiview = [
        'uses HTTP mehods as function (get, post, patch, put, delete)',
        'Traditional django view','Third value',
        'It is mapped manually to URLs'
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Hello serializers POst Method  """

        serializer = serializers.HelloSerializers(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Put method example """

        return Response({'message': 'Put'})

    def patch(self, request, pk=None):
        """ Patch method example """

        return Response({'message': 'Patch'})

    def delete(self, request, pk=None):
        """ Delete method example """

        return Response({'message':'Delete'})

class HelloViewSet(viewsets.ViewSet):
    """ Sample hello viewsets """

    def list(self, request):
        """ A hello Message"""
        a_viewset = [
        'a new view set to create post, get, delete',
        'Automatically map to URLS using rouers',
        'provide more functionality with less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
