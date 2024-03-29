# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Task(models.Model):
    """任务"""
    urgency_choices = (
        (3, '紧急'),
        (2, '一般'),
        (1, '松弛')
    )
    importance_choice = (
        (3, "重要"),
        (2, '一般'),
        (1, '次要')
    )
    title = models.CharField(verbose_name="标题", max_length=120)
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)
    urgency = models.SmallIntegerField(verbose_name="紧急程度", choices=urgency_choices, default=1)
    importance = models.SmallIntegerField(verbose_name="重要程度", choices=importance_choice, default=1)
    detail = models.TextField(verbose_name="详细信息")

class Admin(models.Model):
    '''管理员表'''
    username = models.CharField(verbose_name='用户名', max_length=32, unique=True)
    password = models.CharField(verbose_name='密码', max_length=64)
    def __str__(self):
        return self.username
    

class App01Lifelog(models.Model):
    global_id = models.PositiveBigIntegerField(verbose_name="ID", primary_key=True)
    addtime = models.DateTimeField(verbose_name="添加时间")
    tag = models.CharField(verbose_name="分类", default="日常", max_length=128, blank=False, null=False)
    content = models.TextField(verbose_name="内容")
    weather = models.CharField(verbose_name="天气", max_length=64, null=True, default='')

    location_id_choices = (
            (0, '无'), (1, '环卫局宿舍'), (2, '奥莱'), (3, '老家')
        )
    location_id = models.IntegerField(verbose_name="地址", db_column='location_Id', choices=location_id_choices, default=2)  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'app01_lifelog'
    def __str__(self):
        return self.content        

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LearningAppUserinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'learning_app_userinfo'

# 第二个数据库


class Favormusic(models.Model):
    song = models.CharField(max_length=128)
    songer = models.CharField(max_length=128)
    addtime = models.DateTimeField()
    album = models.CharField(max_length=100, blank=True, null=True)
    info_from = models.IntegerField()
    duration = models.TimeField()
    global_id = models.PositiveBigIntegerField(unique=True)
    native_id = models.CharField(primary_key=True, max_length=18)
    tag = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favormusic'
        unique_together = (('native_id', 'info_from'), ('native_id', 'info_from'),)
        db_tablespace = 'second_db'


class Lifelog(models.Model):
    global_id = models.PositiveBigIntegerField(verbose_name="ID", primary_key=True)
    addtime = models.DateTimeField(verbose_name="添加时间")
    tag = models.CharField(verbose_name="分类", max_length=128, blank=True, null=True)
    content = models.TextField(verbose_name="内容")
    weather = models.CharField(verbose_name="天气", max_length=64, null=True)
    location_id = models.IntegerField(verbose_name="地址", db_column='location_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lifelog'
        db_tablespace = 'second_db'
       

        


