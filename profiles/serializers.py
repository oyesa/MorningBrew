from rest_framework import serializers
from .models import*



class BaseSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        remove_fields = kwargs.pop('remove_fields', None)
        super(BaseSerializer, self).__init__(*args, **kwargs)

        if remove_fields:
            for field_name in remove_fields:
                self.fields.pop(field_name)



class UserProfileSerializer(BaseSerializer):
   
    def __init__(self, *args, **kwargs):
        super(UserProfileSerializer, self).__init__(*args, **kwargs)

    username = serializers.ReadOnlyField(source='fetch_username')
    img_url = serializers.ReadOnlyField(source='fetch_image')
    articles = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    following = serializers.SerializerMethodField()

