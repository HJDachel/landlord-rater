from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PropertySerializer
from .models import Property

# Create your views here.

class PropertyViews(APIView):
    def post(self, request):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id=None):
        if id:
            property = Property.objects.get(id=id)
            serializer = PropertySerializer(property)
            return Response({"status":"success", "data": serializer.data}, status=status.HTTP_200_OK)

        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response({"status":"success", "data": serializer.data}, status=status.HTTP_200_OK)

