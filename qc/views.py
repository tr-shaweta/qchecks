from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inspection
from .serializers import InspectionSerializer

class InspectionView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = InspectionSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            inspection = serializer.save()
            return Response({"status": "success", "data": InspectionSerializer(inspection).data}, status=status.HTTP_201_CREATED)
        return Response({"status": "fail", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


