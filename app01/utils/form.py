from django.utils import timezone
from django.core.exceptions import ValidationError

# ModelForm(实现web添加日志信息)
from django import forms
from app01  import models 

# 导入自定义模块 
from app01.utils.bootstrap_form import BootstrapModelForm
from app01.utils.encrypt import md5
# #雪花ID
from custom_modles import module_snowflake

class LogModeForm(BootstrapModelForm):
    # weather = forms.CharField(required=False)              # 取消input标签的required属性(默认所有inpute标签带有required属性)
    weather = forms.CharField(required=False, 
                              widget=forms.TextInput(attrs={"autocomplete": "off"}))
    class Meta:
        model = models.App01Lifelog # 获取表 
        # fields = ["addtime", "tag", "content", "weather", "location_id"]  # 获取表中的列
        fields = "__all__"                                 # 获取表中的所有列
        # exclude = ["global_id"]                          # 排除列
        widgets = {
            "content": forms.TextInput(attrs={"autocomplete": "off"}),

        }
    
    def __init__(self, *args, **kwargs):  # 定义input标签的class属性
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # 设置addtime默认值: 默认值为当前日期时间
            if field_name == "addtime":
                field.widget.attrs["value"] = timezone.now()
            # 设置global_id默认值: 雪花ID
            elif field_name == "global_id":
                field.widget.attrs["value"] = module_snowflake.IdWorker(1, 1, 0).get_id()

class LogModeForm_exclude(LogModeForm):
    class Meta:
        model = models.App01Lifelog # 获取表 
        # fields = "__all__"                                 # 获取表中的所有列
        exclude = ["global_id"]     # 排除列
        widgets = {
            "content": forms.TextInput(attrs={"autocomplete": "off"}),
        }


class LifeLogEdit(BootstrapModelForm):                         # 专门针对编辑的页面，去除了ID和添加时间的修改，不使用所有字段
    global_id = forms.CharField(disabled=True, label='ID')     # 可看不能改
    addtime = forms.CharField(disabled=True, label='添加时间') # 可看不能改
    weather = forms.CharField(required=False)                  # 取消input标签的required属性(默认所有inpute标签带有required属性)
    class Meta:
        model = models.App01Lifelog # 获取表 
        fields = ["global_id", "addtime", "tag", "content", "weather", "location_id"]  # 获取表中的列，专门针对编辑的页面，去除了ID和添加时间的修改
        # fields = "__all__"                                   # 获取表中的所有列，等同于: fields = ["global_id", "addtime", "tag", "content", "weather", "location_id"]
        # widgets = {
        #     "addtime": forms.TextInput(attrs={"value": "2020"}),
        # }

class Admin_add_ModeForm(BootstrapModelForm):   
    # forms.PasswordInput 输入框密码不因错误而清空
    verify_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)   

    class Meta:
        model = models.Admin  # 获取表 
        # fields = "__all__"    # 获取表中的所有列
        fields = ["username", "password", "verify_password"]
        widgets = {
            "password": forms.PasswordInput
        }

    # 对密码进行MD5加密
    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)
    # 对加密后的密码进行验证
    def clean_verify_password(self):
        # self.clean_passwrod()
        password = self.cleaned_data.get("password")
        verify_password = md5(self.cleaned_data.get("verify_password"))
        if password != verify_password:
            raise ValidationError("密码不一致")
        return verify_password


# class Task_ModeForm(BootstrapModelForm):


class Task_add_ModeForm(BootstrapModelForm):   
    # forms.PasswordInput 输入框密码不因错误而清空
    # verify_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)   
    
    class Meta:
        model = models.Task  # 获取表 
        fields = "__all__"    # 获取表中的所有列
        widgets = {
                    'detail':forms.TextInput,
                   }
        
        # fields = ["username", "password", "verify_password"]
        # widgets = {
        #     "password": forms.PasswordInput
        # }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['detail'].widget.attrs.update({'style': 'width100%;'})


