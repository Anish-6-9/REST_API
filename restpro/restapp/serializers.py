from rest_framework import serializers
from . models import TestModel


class TestSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return TestModel.objects.create(**validated_data)
