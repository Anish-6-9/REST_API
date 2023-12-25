from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializers(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
