from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from authapp.models import FndUser
from .exceptions import *
import json
from .models import*
from .serializers import (UserProfileSerializer,UpdateUserProfileSerializer,UserListSerializer)
# Create your views here.

#class to get user profile
class UserProfileView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserProfileSerializer

    #enpoint to get user data from profle

    def get(self, request, username):
        try:
              profile = Profile.objects.get(user__username=username)
        except Exception:
              return Response({
                  'errors': {
                      'user': ['User does not exist']
                  }
              }, status=status.HTTP_404_NOT_FOUND)
        if request.user.username == username:
            serializer = UserProfileSerializer(
                profile, context={'request': request},
            )
        return Response({
            'profile': serializer.data
        }, status=status.HTTP_200_OK)