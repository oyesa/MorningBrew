from dataclasses import fields
from statistics import mode
from rest_framework.serializers import ModelSerializer
from .models import *

class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['name','image','description','category','phone_number']
        # exclude = ['id']
        # depth = 1

class RatingsSerializer(ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['service','skills','time','affordability',]
        # fields = '__all__'
        # exclude = (id)