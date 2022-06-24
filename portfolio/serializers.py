from rest_framework import serializers
from .models import *


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['artisan','phone_no','description','image']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['name','comment','date']
        date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")