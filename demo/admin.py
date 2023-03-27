from django.contrib import admin


from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')      # 列表可编辑跳转链接
    fieldsets = [
        ('基础信息', {'fields': [('title', 'pub_date'),'content']})
        # ('', {'fields': ['content']})
    ]

admin.site.register(Article,ArticleAdmin)