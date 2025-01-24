from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

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

        if extra_fields.get('is_staff') is not True:
            raise ValueError('超级用户必须设置is_staff为True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('超级用户必须设置is_superuser为True')

        return self._create_user(real_name, email, password, **extra_fields)


# 用户状态
class UserStatusChoices(models.ModelChoices):
    ACTIVED = 1
    UNACTIVE = 2
    LOCK = 3

# 重写user模型
class OAUserModel(AbstractBaseUser, PermissionsMixin):
    """
        自定义的User模型
    """
    real_name = models.CharField(max_length=150, unique=False, verbose_name='真实姓名')
    email = models.EmailField(unique=True, blank=False, verbose_name='邮箱')
    telephone = models.CharField(max_length=20, blank=True, verbose_name='手机号')
    is_staff = models.BooleanField(default=True, verbose_name='员工用户')
    status = models.IntegerField(choices=UserStatusChoices.choices, default=UserStatusChoices.UNACTIVE, verbose_name='用户状态')
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')

    objects = OAUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

