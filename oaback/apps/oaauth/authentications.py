import jwt
import time
from django.conf import settings
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
from jwt.exceptions import ExpiredSignatureError

from .models import OAUser


def generate_jwt(user):
    timestamp = int(time.time()) + 60*60*24*7
    return jwt.encode({'userid':user.pk,'exp':timestamp}, settings.SECRET_KEY, algorithm='HS256')

class UserTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        return request._request.user, request._request.auth

class JWTAuthentication(BaseAuthentication):

    keyword = 'jwt'

    def authenticate_header(self, request):

        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = '令牌不可用！'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = '令牌不可用！'
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_info = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=['HS256'])
            userid = jwt_info.get('userid')
            try:
                user = OAUser.objects.get(pk=userid)
                setattr(request, 'user', user)
                return user, jwt_token
            except:
                msg = '用户不存在！'
                raise exceptions.AuthenticationFailed(msg)
        except ExpiredSignatureError:
            msg = '令牌已过期！'
            raise exceptions.AuthenticationFailed(msg)