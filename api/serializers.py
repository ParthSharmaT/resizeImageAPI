from rest_framework import serializers
from .models import FishRecord

class FishRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishRecord
        fields ='__all__'
