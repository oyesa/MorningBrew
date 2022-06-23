from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
# from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

@api_view(['GET', 'PUT', 'DELETE'])
def showportfolio(request, pk):
    """
    Retrieve, update or delete a code contact.
    """
    try:
       Portfolio= Portfolio.objects.get(id=pk)
    except Portfolio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer =PortfolioSerializer(Portfolio)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PortfolioSerializer(Portfolio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Portfolio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()