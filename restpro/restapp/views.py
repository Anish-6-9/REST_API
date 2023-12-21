from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
from rest_framework.decorators import APIView
from rest_framework import status
from . models import TestModel
from . serializers import TestSerializers


class TestView(APIView):
    def get(self, request):
        try:
            data = TestModel.objects.all()
            # query set to native python data ->query set
            serializers = TestSerializers(data, many=True)
            return JsonResponse({"data": serializers.data}, status=200)
        except Exception as exe:
            print(exe)
            return JsonResponse({"message": "Internal server error"}, status=500)

    def post(self, request):
        try:
            serializer = TestSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"data": "Data successfully save"}, status=200)

            return JsonResponse({"data": serializer.errors}, status=400)

        except Exception as exe:
            print(exe)
            return JsonResponse({"message": "Internal server error"}, status=500)
