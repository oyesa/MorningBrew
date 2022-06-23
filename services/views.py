from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .forms import *
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ServiceSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
class ServiceViewSet(ModelViewSet):
    serializer_class=ServiceSerializer
    queryset=Service.objects.all()
class ServiceList(APIView):
    def get(self, request, format=None):
        all_services = Service.objects.all()
        serializers = ServiceSerializer(all_services, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ServiceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    permission_classes = (IsAdminOrReadOnly,)

@api_view(['GET', 'PUT', 'DELETE'])
def showservice(request, pk):
    """
    Retrieve, update or delete a code contact.
    """
    try:
       Service= Service.objects.get(id=pk)
    except Service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =ServiceSerializer(Service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializer(Service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RatingsViewSet(ModelViewSet):
    serializer_class=RatingsSerializer
    queryset=Ratings.objects.all()

