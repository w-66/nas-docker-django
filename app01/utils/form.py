from django.utils import timezone
# 导入自定义模块 雪花ID
from custom_modles import module_snowflake
from app01.utils.bootstrap_form import BootstrapModelForm
# ModelForm(实现web添加日志信息)
from django import forms
from app01  import models 

class LogModeForm(BootstrapModelForm):
    weather = forms.CharField(required=False)              # 取消input标签的required属性(默认所有inpute标签带有required属性)

    class Meta:
        model = models.App01Lifelog # 获取表 
        # fields = ["addtime", "tag", "content", "weather", "location_id"]  # 获取表中的列
        fields = "__all__"                                 # 获取表中的所有列
        # widgets = {
        #     "addtime": forms.TextInput(attrs={"value": "2020"}),
        # }
    
    def __init__(self, *args, **kwargs):  # 定义input标签的class属性
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # 设置addtime默认值: 默认值为当前日期时间
            if field_name == "addtime":
                field.widget.attrs["value"] = timezone.now()
            # 设置global_id默认值: 雪花ID
            elif field_name == "global_id":
                field.widget.attrs["value"] = module_snowflake.IdWorker(1, 1, 0).get_id()

             

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
    