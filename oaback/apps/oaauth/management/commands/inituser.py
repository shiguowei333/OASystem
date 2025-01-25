from django.core.management.base import BaseCommand
from apps.oaauth.models import OAUser, OADepartment


class Command(BaseCommand):
    def handle(self, *args, **options):

        boarder = OADepartment.objects.get(name='董事会',)
        developer = OADepartment.objects.get(name='产品开发部',)
        operator = OADepartment.objects.get(name='运营部')
        saler = OADepartment.objects.get(name='销售部')
        hr = OADepartment.objects.get(name='人事部')
        finance = OADepartment.objects.get(name='财务部')

        baizhantang = OAUser.objects.create_superuser(email='baizhantang@qq.com', real_name='白展堂', password='123456',department=boarder)
        tongxiangyu = OAUser.objects.create_superuser(email='tongxiangyu@qq.com', real_name='佟湘玉', password= '123456', department=boarder)

        lvqinghou = OAUser.objects.create_user(email='lvqinghou@qq.com', real_name='吕轻侯', password='123456',department=developer)
        guofurong = OAUser.objects.create_user(email='guofurong@qq.com', real_name='郭芙蓉', password='123456',department=finance)
        moxiaobei = OAUser.objects.create_user(email='moxiaobei@qq.com', real_name='莫小贝', password='123456',department=hr)
        lixiulian = OAUser.objects.create_user(email='lixiulian@qq.com', real_name='李秀莲', password='123456',department=operator)
        zhuwushuang = OAUser.objects.create_user(email='zhuwushuang@qq.com', real_name='祝无双', password='123456',department=saler)

        boarder.leader = baizhantang
        boarder.manager = None
        boarder.save()

        developer.leader = lvqinghou
        developer.manager = baizhantang
        developer.save()

        operator.leader = lixiulian
        operator.manager = baizhantang
        operator.save()

        saler.leader = zhuwushuang
        saler.manager = baizhantang
        saler.save()

        hr.leader = moxiaobei
        hr.manager = tongxiangyu
        hr.save()

        finance.leader = guofurong
        finance.manager = tongxiangyu
        finance.save()

        self.stdout.write('初始化用户创建成功！')

