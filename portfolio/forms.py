from django import forms
from .models import *
from rest_framework import viewsets

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PortfolioSerializer