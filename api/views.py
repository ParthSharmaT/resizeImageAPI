from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import FishRecord
from .serializers import FishRecordSerializer
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

class FishRecordViewSet(APIView):
    def post(self,request):
        serializer=FishRecordSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'message':'done'})
        return Response(serializer.errors)


    def get(self,request):
        data=FishRecord.objects.all().order_by('created_at').reverse()
        serializer=FishRecordSerializer(data,many=True)
        return Response(serializer.data)   
