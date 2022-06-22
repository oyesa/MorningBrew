from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ServiceSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

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

