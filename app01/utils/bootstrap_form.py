from django import forms


class BootstrapModelForm(forms.ModelForm):
    # 定义input标签的class属性
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        # 循环所有modelform中的字段，给每个字段设置属性
        for field_name, field in self.fields.items():
            if field.widget.attrs:            # 如果原本class有值则新增一个class 属性
                field.widget.attrs["class"] = "form-control"
            else:                             # 否则直接添加
                field.widget.attrs = {        # 把需要的默认值直接赋值给了 field.widget.attrs 字典，例外需要定义的标签class再单独设置
                    "class": "form-control"
                }

