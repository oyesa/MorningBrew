from .views import *
from django.urls import path

urlpatterns = [
  path('register', UserProfileView.as_view(), name='AuthRegistry'),

   
]