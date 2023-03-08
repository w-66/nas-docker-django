from django.contrib import admin
from .models import Lifelog,Tag



### v6 优化 Question 变更页：添加侧边过滤器; 增加搜索功能; 分页
class TagInline(admin.TabularInline):
    model = Tag
    extra = 3  #这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”

class LifelogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [TagInline]      # 调用ChoiceInline
    list_display = ('title_text', 'pub_date')  
    list_filter = ['pub_date']    # 新增代码
    search_fields = ['title_text', 'pub_date']
    # list_per_page = 2
    date_hierarchy = 'pub_date'



admin.site.register(Lifelog,LifelogAdmin)