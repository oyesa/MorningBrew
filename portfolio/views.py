from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *



# Create your views here.
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer