from django.forms import ValidationError
from rest_framework import serializers
from .models import FndUser
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=150,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = FndUser
        fields = ['email', 'username', 'password', 'first_name']

    def create(self, validated_data):
        return FndUser.objects.create_user(**validated_data)