from rest_framework import serializers
from .models import OAUser, UserStatusChoices, OADepartment


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=20, min_length=6, required=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = OAUser.objects.filter(email=email).first()
            if not user:
                raise serializers.ValidationError('用户不存在！')
            if not user.check_password(password):
                raise serializers.ValidationError('密码错误！')
            if user.status == UserStatusChoices.UNACTIVE:
                raise serializers.ValidationError('该用户未激活！')
            elif user.status == UserStatusChoices.LOCKED:
                raise serializers.ValidationError('该用户已被锁定！')
            attrs['user'] = user
        else:
            raise serializers.ValidationError('请输入邮箱和密码！')
        return attrs

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OADepartment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = OAUser
        exclude = ('password', 'groups', 'user_permissions')