from rest_framework import serializers
from .models import *


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = __all__
