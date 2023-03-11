from django.contrib import admin
from .models import Lifelog,Tag
from django.db import models
from django.utils import html

@admin.display(empty_value='Null')    # empty_value_display = '-empty-' # 该属性覆盖记录字段为空（None、空字符串等）的默认显示值。默认值是 - （破折号）。
class LifelogAdmin(admin.ModelAdmin):
    #  “添加” 和 “更改” 页面的布局
    fieldsets = [
        ('基础信息', {
            'fields': ['pub_date','tags', 'location'],
            # 'classes': ['wide']
            # 'description': '日期'
        }),
        (None, {
            'fields': ['content']
        }),
    ]
    # 外部列表视图
    # inlines = [TagInline]                    # 调用ChoiceInline
    list_display = ('formatted_pub_date', 'location','content')      
                                               # 列表 blog表中的数据列表
    def formatted_pub_date(self, obj):         # 自定义pub_date的格式
        return html.format_html(
            '<span style="color: DeepSkyBlue;">{}</span>',
            obj.pub_date.strftime("%Y-%m-%d %H:%M")
        )
    formatted_pub_date.short_description = '记录日期'
        
    # list_filter = ['pub_date']               # 过滤选项
    search_fields = ['pub_date', 'content','tags__tag']    
                                               # 搜索 
                                               # tags__tag 表示关联查询，它告诉Django ORM搜索tags字段的相关(相关联的)模型（即Tag模型），并使用tag字段进行搜索。
    list_per_page = 20                         # 一页上限
    date_hierarchy = 'pub_date'                # 时间筛选
    list_max_show_all = 200                    # default 控制 “全部显示” 的管理员更改列表页面上可以出现多少个项目。
    autocomplete_fields = ['tags']             # use select2 to select user   

class TagAdmin(admin.ModelAdmin):
    search_fields = ['tag']    # 搜索


admin.site.register(Lifelog,LifelogAdmin)
admin.site.register(Tag,TagAdmin)