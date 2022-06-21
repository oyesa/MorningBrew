from django.forms import ValidationError
from rest_framework import serializers
from .models import FndUser
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from authors.utils.password_validators import get_password_policy_errors

# Request and create a new user
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=150,
        min_length=8,
        write_only=True, 
        required=True
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=FndUser.objects.all(),
                message='user with this email already exists'
            )
        ]
    )
    def validate_password(self, value):
        errors = get_password_policy_errors(value)
        if errors:
            raise serializers.ValidationError(errors)
        return value

    class Meta:
        model = FndUser
        fields = ['email', 'username', 'password', 'first_name']

    def create(self, validated_data):
        return FndUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255, allow_blank=True)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True, allow_blank=True)
    token = serializers.CharField(max_length=255, read_only=True)

#method to validate that what the user logged in is what is in the database
    def validate(self, data):
