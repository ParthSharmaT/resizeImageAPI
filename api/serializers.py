from rest_framework import serializers
from .models import FishRecord

class FishRecordSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta():
        model = FishRecord
        fields = ('title','weight','length','latitude','longitude','created_at','updated_at','image')
