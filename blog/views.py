from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Lifelog, Article

# 网页图标logo
# site_logo = 'icon-logo-1' 替换成本地路径的logo
def index(request):
    title = 'Blog'
    dict = {
        'title':title,
    }
    return render(request, 'blog/index.html', dict)
    

class Lifelog_ListView(generic.ListView):
    template_name = 'blog/lifelog.html'
    context_object_name = 'queryset'
    paginate_by = 6
    def get_queryset(self):
        return Lifelog.objects.order_by('-pub_date')

from django import forms

class Article_ListView(generic.ListView):
    # pass
    template_name = 'blog/article_list.html'
    context_object_name = 'queryset'
    def get_queryset(self):
        return Article.objects.order_by('-pub_date')
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)    # 从名为“Article”的模型中获取一个主键（pk）等于给定值，如果该实例不存在，则引发HTTP 404异常。
    md_content = str(article.content)
    
    return render(request, 'blog/article_detail.html', {'md_content':md_content})

