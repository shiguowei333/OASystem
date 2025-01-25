from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from shortuuidfield import ShortUUIDField

# 用户状态
class UserStatusChoices(models.IntegerChoices):
    ACTIVED = 1
    UNACTIVE = 2
    LOCKED = 3

class OAUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, real_name, email, password, **extra_fields):
        """
            创建用户
        """
        if not real_name:
            raise ValueError('必须设置真实姓名！')
        email = self.normalize_email(email)
        user = self.model(real_name=real_name, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, real_name, email, password=None, **extra_fields):
        """
            创建普通用户
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(real_name, email, password, **extra_fields)

    def create_superuser(self, real_name, email, password=None, **extra_fields):
        """
            创建超级用户
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('status', UserStatusChoices.ACTIVED)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('超级用户必须设置is_staff为True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('超级用户必须设置is_superuser为True')

        return self._create_user(real_name, email, password, **extra_fields)



# 重写user模型
class OAUser(AbstractBaseUser, PermissionsMixin):
    """
        自定义的User模型
    """
    uid = ShortUUIDField(primary_key=True)
    real_name = models.CharField(max_length=150, unique=False, verbose_name='真实姓名')
    email = models.EmailField(unique=True, blank=False, verbose_name='邮箱')
    telephone = models.CharField(max_length=20, blank=True, verbose_name='手机号')
    is_staff = models.BooleanField(default=True, verbose_name='员工用户')
    status = models.IntegerField(choices=UserStatusChoices.choices, default=UserStatusChoices.UNACTIVE, verbose_name='用户状态')
    is_active = models.BooleanField(default=True, verbose_name='是否激活')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    department = models.ForeignKey('OADepartment', null=True, on_delete=models.SET_NULL, related_name='staffs', related_query_name='staffs', verbose_name='所属部门')

    objects = OAUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['real_name', 'password']

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        return self.real_name

    def get_short_name(self):
        return self.real_name


# 部门表模型
class OADepartment(models.Model):
    name = models.CharField(max_length=100, verbose_name='部门名称')
    intro = models.CharField(max_length=200, verbose_name='部门介绍')
    leader = models.OneToOneField(OAUser, null=True, on_delete=models.SET_NULL, related_name='leader_department', related_query_name='leader_department', verbose_name='部门经理')
    manager = models.ForeignKey(OAUser, null=True, on_delete=models.SET_NULL, related_name='manager_departments', related_query_name='manager_departments', verbose_name='部门领导')