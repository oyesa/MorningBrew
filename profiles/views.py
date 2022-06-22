from django.shortcuts import render
from django.core.exceptions import ValidationError
from rest_framework.exceptions import APIException
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from authapp.models import FndUser

import json
from .models import*
from .serializers import (UserProfileSerializer)
# Create your views here.


class UserProfileView(GenericAPIView):
  pass