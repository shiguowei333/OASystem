from django.db import models
from django.contrib.auth import get_user_model

OAUser = get_user_model()

class AbsentStatusChoices(models.IntegerChoices):
    AUDITING = 1
    PASS = 2
    REJECT = 3

class AbsentType(models.Model):
    name = models.CharField(max_length=100, verbose_name='请假类型')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

class Absent(models.Model):
    title = models.CharField(max_length=200, verbose_name='请假标题')
    request_content = models.TextField(verbose_name='请假内容')
    absent_type = models.ForeignKey(AbsentType, on_delete=models.CASCADE, verbose_name='请假类型', related_name='absents', related_query_name='absents')
    requester = models.ForeignKey(OAUser, on_delete=models.CASCADE, verbose_name='请假人', related_name='my_absents', related_query_name='my_absents')
    responder = models.ForeignKey(OAUser, on_delete=models.CASCADE, verbose_name='审批人', related_name='sub_absents', related_query_name='sub_absents', null=True)
    status = models.IntegerField(choices=AbsentStatusChoices, default=AbsentStatusChoices.AUDITING, verbose_name='审核状态')
    start_date = models.DateField(verbose_name='开始日期')
    end_date = models.DateField(verbose_name='结束日期')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='请假发起时间')
    response_content = models.TextField(verbose_name='审批意见')
