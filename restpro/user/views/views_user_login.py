from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.http import JsonResponse
from django.contrib.auth import authenticate

from user import global_message
from user import login_validation


class UserLoginView(APIView):
    def post(self, request):
        try:
            error_list, username, password = login_validation.user_login(
                request)
            if error_list:
                return JsonResponse({global_message.RESPONSE_KEY: error_list}, status=status.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                message = {
                    "username": user.username,
                    "email": user.email,
                    "token": token.key
                }
            return JsonResponse({global_message.RESPONSE_KEY: "test"}, status=status.HTTP_200_OK)
        except Exception as exe:
            print(exe)
            return JsonResponse({global_message.RESPONSE_KEY: global_message.WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
