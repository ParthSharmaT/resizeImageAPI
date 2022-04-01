from rest_framework import serializers
from .models import FishRecord

class FishRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishRecord
        fields = ('title', 'image', 'weight', 'length', 'created_at', 'updated_at')
        