from django.shortcuts import render
from .models import *
from rest_framework import viewsets


# Create your views here.
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PortfolioSerializer