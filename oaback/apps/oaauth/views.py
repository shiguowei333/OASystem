from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer
from datetime import datetime
from .authentications import generate_jwt
from rest_framework.permissions import IsAuthenticated
from .serializers import ResetPwdSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.last_login = datetime.now()
            user.save()
            token = generate_jwt(user)
            return Response({'token': token, 'user': UserSerializer(user).data})
        else:
            print(serializer.errors)
            return Response({'detail': '登录验证失败！'}, status=status.HTTP_400_BAD_REQUEST)


class ResetPwdView(APIView):
    def post(self, request):
        serializer = ResetPwdSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            request.user.set_password(serializer.validated_data.get('pwd1'))
            request.user.save()
            return Response({'detail': '密码修改成功！'})
        else:
            detail = list(serializer.errors.values())[0][0]
            print(detail)
            return Response({'detail': '密码修改失败！'}, status=status.HTTP_400_BAD_REQUEST)