import base64

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


def user_login(request):
    error_list = []
    auth_data = request.META['HTTP_AUTHORIZATION']
    encoded_data = auth_data.split(' ')[1]
    decodede_data = base64.b64decode(encoded_data).decode('utf-8').split(':')
    username = decodede_data[0]
    password = decodede_data[1]
    print(decodede_data)

    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        if not check_password(password, user.password):
            error_list.append("invalid username/password")
    else:
        error_list.append("No such user")

    return error_list, username, password
