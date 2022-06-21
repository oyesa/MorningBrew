from .views import RegistrationAPIView
from django.urls import path, re_path

urlpatterns = [
    path('register', RegistrationAPIView.as_view(), name='AuthRegistry')
]