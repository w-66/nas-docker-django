from django.contrib import admin
from .models import Loglife


# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['title_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]      # 调用ChoiceInline
#     list_display = ('question_text', 'pub_date', 'was_published_recently')  
#     list_filter = ['pub_date']    # 新增代码
#     search_fields = ['question_text', 'pub_date']
#     # list_per_page = 2
#     date_hierarchy = 'pub_date'

admin.site.register(Loglife)