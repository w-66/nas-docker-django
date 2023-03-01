from django.contrib import admin
from .models import Question,Choice

### v6 优化 Question 变更页：添加侧边过滤器; 增加搜索功能; 分页
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  #这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]      # 调用ChoiceInline
    list_display = ('question_text', 'pub_date', 'was_published_recently')  
    list_filter = ['pub_date']    # 新增代码
    search_fields = ['question_text', 'pub_date']
    # list_per_page = 2
    date_hierarchy = 'pub_date'
admin.site.register(Question, QuestionAdmin)

### v5 自定义后台更改列表
# 让我们对“更改列表”页面进行一些调整——改成一个能展示系统中所有投票的页面。
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3  #这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]  # 调用ChoiceInline
#     list_display = ('question_text', 'pub_date', 'was_published_recently')  # 新增代码
# admin.site.register(Question, QuestionAdmin)

### v4 对于选项 更好的办法是在你创建“投票”对象时直接添加好几个选项。让我们实现它。
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3  #这会告诉 Django：“Choice 对象要在 Question 后台页面编辑。默认提供 3 个足够的选项字段。”

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]  # 调用ChoiceInline

# admin.site.register(Question, QuestionAdmin)

### v3 说到拥有数十个字段的表单，你可能更期望将表单分为几个字段集
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
# admin.site.register(Question, QuestionAdmin)

### v2 以下修改使得 "Publication date" 字段显示在 "Question" 字段之前
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']  # 发布时间在第一列

# admin.site.register(Question, QuestionAdmin)

### v1
# admin.site.register(Question)

