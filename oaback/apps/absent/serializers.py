from logging import exception

from rest_framework import serializers, exceptions
from apps.oaauth.serializers import UserSerializer
from apps.absent.models import Absent, AbsentType, AbsentStatusChoices

class AbsentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbsentType
        fields = '__all__'

class AbsentSerializer(serializers.ModelSerializer):
    absent_type = AbsentTypeSerializer(read_only=True)
    absent_type_id = serializers.IntegerField(write_only=True)
    requester = UserSerializer(read_only=True)
    responder = UserSerializer(read_only=True)
    class Meta:
        model = Absent
        fields = '__all__'

    def validate_type_id(self, value):
        if not AbsentType.objects.filter(pk=value).exists():
            raise exceptions.ValidationError('请假类型不存在')
        return value
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        if user.department.leader.uid == user.uid:
            if user.department.name == '董事会':
                responder = None
            else:
                responder = user.department.manager
        else:
            responder = user.department.leader

        if responder is None:
            validated_data['status'] = AbsentStatusChoices.PASS
        else:
            validated_data['status'] = AbsentStatusChoices.AUDITING
        return Absent.objects.create(**validated_data, responder=responder, requester=user)


    def update(self, instance, validated_data):
        if instance.status == AbsentStatusChoices.AUDITING:
            raise exceptions.APIException('该请假单已审批')
        request = self.context['request']
        user = request.user
        if instance.responder.uid != user.uid:
            raise exceptions.AuthenticationFailed('您无权处理该考勤')
        instance.status = validated_data.get('status', instance.status)
        instance.response_content = validated_data['response_content']
        instance.save()
        return instance
