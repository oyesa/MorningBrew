from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserJSONRenderer
from rest_framework import status
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView

from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import (RegistrationSerializer,LoginSerializer,FndUserSerializer)


# Create views here.
class RegistrationAPIView(APIView):
    
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegistrationSerializer
    
    def post(self, request):
       
        user = request.data.get('FndUser', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


#login a user
class LoginApiView(GenericAPIView):
    permission_classes =(AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self,request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#get a user and update

class FndUserRetrieveupdateApiView(RetrieveUpdateAPIView):
     permission_classes = (IsAuthenticated,)
     renderer_classes = (UserJSONRenderer,)
     serializer_class = FndUserSerializer












