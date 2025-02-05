import jwt
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from jwt.exceptions import ExpiredSignatureError
from rest_framework import exceptions
from rest_framework.authentication import get_authorization_header
from django.http.response import JsonResponse
from apps.oaauth.models import OAUser
from rest_framework.status import HTTP_403_FORBIDDEN
from django.contrib.auth.models import AnonymousUser


class LoginMiddleware(MiddlewareMixin):
    keyword = 'jwt'
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.path == '/auth/login':
            request.user = AnonymousUser()
            request.auth = None
            return None
        try:
            auth = get_authorization_header(request).split()

            if not auth or auth[0].lower() != self.keyword.lower().encode():
                raise exceptions.ValidationError('请传入JWT！')

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
                    request.user = user
                    request.auth = jwt_token
                except:
                    msg = '用户不存在！'
                    raise exceptions.AuthenticationFailed(msg)
            except ExpiredSignatureError:
                msg = '令牌已过期！'
                raise exceptions.AuthenticationFailed(msg)
        except Exception as e:
            print(e)
            return JsonResponse({'detail': '请先登录!'}, status=HTTP_403_FORBIDDEN)