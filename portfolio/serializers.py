from rest_framework import serializers
from .models import *


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['artisan','phone_no','description','image']
