from django.contrib import admin
from django.db import models
from .widgets import VditorWidget

from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')      # 列表可编辑跳转链接

    fieldsets = [
        ('基础信息', {
            'fields': ['title', 'pub_date'],
        }),
        (None, {
            'fields': ['content']
        }),
    ]

    formfield_overrides = {
        models.TextField: {'widget': VditorWidget}
    }




    # change_form_template = 'demo/change_form_with_vditor.html'
    # class Media:                              # 加载静态资源
    #     css = {
    #         "all": ('plugin/vditor/index.min.js',)
    #     }
    #     js = ('plugin/vditor/index.min.js',)

admin.site.register(Article,ArticleAdmin)