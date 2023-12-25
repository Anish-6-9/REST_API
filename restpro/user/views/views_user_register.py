from django.http import JsonResponse
from django.contrib.auth.models import User


from rest_framework.decorators import APIView
from rest_framework import status


from user.serializers import UserSerializers

from user import global_message


class UserRegisterView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializers = UserSerializers(users, many=True)
            return JsonResponse({global_message.RESPONSE_KEY: global_message.MESSAGE, "data": serializers.data}, status=status.HTTP_200_OK)
        except Exception as exe:
            print(exe)
            return JsonResponse({global_message.RESPONSE_KEY: global_message.WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializers = UserSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({global_message.RESPONSE_KEY: global_message.SUCCESS}, status=status.HTTP_200_OK)
            return JsonResponse({global_message.RESPONSE_KEY: serializers.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            print(exe)
            return JsonResponse({global_message.RESPONSE_KEY: global_message.WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
